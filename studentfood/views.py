from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Recipe, User, Comment
from django.http import Http404
from .forms import CommentForm, RecipeForm
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.

def main(request):  # лист рецептов
    search_query = request.GET.get('search', '')
    category_query = request.GET.get('category_button', '')
    null_recipe = Recipe()
    raw_category = null_recipe.GLOBAL_CATEGORY
    site_category = []
    for elem in raw_category:
        site_category.append(elem[1])
    if search_query:
        recipes_list = Recipe.objects.filter(
            Q(recipe_name__icontains=search_query) | Q(description__icontains=search_query))
    elif category_query:
        for raw in raw_category:
            if category_query == raw[1]:
                recipes_list = Recipe.objects.filter(Q(category__exact=raw[0]))
    else:
        recipes_list = Recipe.objects.order_by('-pub_date')
    paginator = Paginator(recipes_list, 3)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    context = {'recipes_list': recipes_list,
               'page': page,
               'recipes': recipes,
               'site_category': site_category,
              }
    return render(request, 'studentfood/html/main.html', context)


def detail(request, recipe_id):  # объект (написать список полей)
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    comment_list = recipe_detail.comment_set.all()
    comments_count = comment_list.count()
    comment_form = CommentForm()
    post_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        post_comment = Comment()
        if comment_form.is_valid():
            post_comment.text = comment_form.cleaned_data.get("text")
            post_comment.recipe = get_object_or_404(Recipe, pk=recipe_id)
            post_comment.user = request.user
            post_comment.save()

    context = {'recipe_detail': recipe_detail,
               'comment_list': comment_list,
               'comment_form': comment_form,
               'post_comment': post_comment,
               'comments_count' : comments_count
              }
    return render(request, 'studentfood/html/product.html', context)


def profile(request):  # пользовательские данные (при переходе возвращает объект пользователя)
    recipes_list = Recipe.objects.order_by()
    recipe_form = RecipeForm()
    # Создание рецепта

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        post_recipe = Recipe()
        if recipe_form.is_valid():
            post_recipe.recipe_name = recipe_form.cleaned_data.get("recipe_name")
            post_recipe.description = recipe_form.cleaned_data.get("description")
            post_recipe.price = recipe_form.cleaned_data.get("price")
            post_recipe.user = request.user
            post_recipe.category = recipe_form.cleaned_data.get("category")
            if 'photo' in request.FILES:  # проверка на то, есть ли в реквесте фотки
                post_recipe.photo = request.FILES['photo']  # если есть, то присваиваем сохраняемому рецепту
            post_recipe.save()
        else:
            return render_to_response('template_name', message='Ошибка добавления рецептов')

    context = {'recipes_list': recipes_list,
               'recipe_form': recipe_form,
              }
    return render(request, 'studentfood/html/profiles/profile.html', context)


# def set_mark


"""def create_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            recipe_form = RecipeForm()
            recipe_form.user = request.user
            return render(request, 'studentfood/html/profiles/profile.html', {'recipe_form': recipe_form,
                                                                                        'request': request})
        if request.method == 'POST':
            recipe_form = RecipeForm(request.POST)
            post_recipe = Recipe()
            if recipe_form.is_valid():
                post_recipe.recipe_name = recipe_form.cleaned_data.get("recipe_name")
                post_recipe.description = recipe_form.cleaned_data.get("description")
                post_recipe.price = recipe_form.cleaned_data.get("price")
                post_recipe.user = request.user
                post_recipe.category = recipe_form.cleaned_data.get("category")
                post_recipe.save()
                return render(request, 'studentfood/html/profiles/profile.html')
            else:
                return HttpResponse('Ваша форма недействительна!')
    else:
        return HttpResponse('Сначала нужно авторизироваться!')"""
