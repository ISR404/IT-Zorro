from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import Recipe, User, Comment
from django.http import Http404
from .forms import CommentForm, RecipeForm


# Create your views here.

def main(request):  # лист рецептов,
    search_query = request.GET.get('search', '')
    if search_query:
        recipes_list = Recipe.objects.filter(recipe_name__icontains=search_query)
    else:
        recipes_list = Recipe.objects.order_by('-pub_date')
    null_recipe = Recipe()
    raw_category = null_recipe.GLOBAL_CATEGORY
    site_category = []
    first_arg = []
    for elem in raw_category:
        site_category.append(elem[1])
        first_arg.append(elem[0])
    context = {'recipes_list': recipes_list,
               'site_category': site_category,
               'first_arg': first_arg,
               'raw_category': raw_category
               }
    return render(request, 'studentfood/html/main.html', context)


def detail(request, recipe_id):  # объект (написать список полей)
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    comment_list = recipe_detail.comment_set.order_by('pub_date')
    if request.user.is_authenticated:
        if request.method == 'GET':
            comment_form = CommentForm()

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            post_comment = Comment()
            if comment_form.is_valid():
                post_comment.text = comment_form.cleaned_data.get("text")
                post_comment.recipe = get_object_or_404(Recipe, pk=recipe_id)
                post_comment.user = request.user
                post_comment.save()
                return render(request, 'studentfood/html/product.html', {'recipe_detail': recipe_detail,
                                                                         'comment_form': comment_form,
                                                                         'comment_list': comment_list})

    return render(request, 'studentfood/html/product.html', {'recipe_detail': recipe_detail,
                                                             'comment_list': comment_list})


def register(request):  # реализация Димы
    return render(request, 'profiles/register.html')


def profile(request):  # пользовательские данные (при переходе возвращает объект пользователя)
    return render(request, 'profiles/profile.html')


def create_recipe(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            recipe_form = RecipeForm()
            recipe_form.user = request.user
            return render(request, 'studentfood/backend-temp/test_recipe_create.html', {'recipe_form': recipe_form,
                                                                                        'request': request})
        if request.method == 'POST':
            recipe_form = RecipeForm(request.POST, request.FILES)
            post_recipe = Recipe()
            if recipe_form.is_valid():
                if 'photo' in request.FILES:  # проверка на то, есть ли в реквесте фотки
                    post_recipe.photo = request.FILES['photo']  # если есть, то присваиваем сохраняемому рецепту
                post_recipe.recipe_name = recipe_form.cleaned_data.get("recipe_name")
                post_recipe.description = recipe_form.cleaned_data.get("description")
                post_recipe.price = recipe_form.cleaned_data.get("price")
                post_recipe.user = request.user
                post_recipe.category = recipe_form.cleaned_data.get("category")
                post_recipe.save()
                return render(request, 'studentfood/backend-temp/test_recipe_create.html')
            else:
                return HttpResponse('Ваша форма недействительна!')
    else:
        return HttpResponse('Сначала нужно авторизироваться!')



