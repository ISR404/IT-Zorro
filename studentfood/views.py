from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, User, Comment, Mark, BookMark
from .forms import CommentForm, RecipeForm, ChangePasswordForm, MarkForm
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
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    context = {'recipes_list': recipes_list,
               'page_obj': page_obj,
               'site_category': site_category
              }
    return render(request, 'studentfood/html/main_page/main.html', context)


def detail(request, recipe_id):  # объект (написать список полей)
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    comment_list = recipe_detail.comment_set.all()
    comments_count = comment_list.count()
    marks_list = recipe_detail.mark_set.all()
    bookmark_list = recipe_detail.bookmark_set.all()
    bookmark_user_ids = []
    for row in bookmark_list:
        bookmark_user_ids.append(row.user_added.id)
    comment_form = CommentForm()
    mark_form = MarkForm()
    post_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        post_comment = Comment()
        mark_form = MarkForm(request.POST)
        post_mark = Mark()

        if comment_form.is_valid():
            post_comment.text = comment_form.cleaned_data.get("text")
            post_comment.recipe = get_object_or_404(Recipe, pk=recipe_id)
            post_comment.user = request.user
            post_comment.save()
            return redirect('studentfood:detail', recipe_id)

        elif mark_form.is_valid():
            for usr in marks_list:
                if usr.user == request.user:
                    edit_mark = recipe_detail.mark_set.get(user=request.user)
                    edit_mark.mark_value = mark_form.cleaned_data.get('mark_value')
                    edit_mark.save()
                    return redirect('studentfood:detail', recipe_id)
            post_mark.mark_value = mark_form.cleaned_data.get('mark_value')
            post_mark.user = request.user
            post_mark.recipe = get_object_or_404(Recipe, pk=recipe_id)
            post_mark.save()
            return redirect('studentfood:detail', recipe_id)

    context = {'recipe_detail': recipe_detail,
               'comment_list': comment_list,
               'comment_form': comment_form,
               'post_comment': post_comment,
               'comments_count': comments_count,
               'mark_form': mark_form,
               'bookmark_user_ids': bookmark_user_ids
              }

    return render(request, 'studentfood/html/detail_recipe/product.html', context)


@login_required
def favourite_add(request, recipe_id):
    if request.method == 'POST':
        request.user.bookmark_set.create(added_recipe=get_object_or_404(Recipe, pk=recipe_id), user_added=request.user)
    return redirect('studentfood:detail', recipe_id)


def profile(request):  # пользовательские данные (при переходе возвращает объект пользователя)
    recipes_list = Recipe.objects.order_by()
    favorite_list = request.user.bookmark_set.all()
    recipe_form = RecipeForm()
    cp_form = ChangePasswordForm()

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
            recipe_form.clean()

    # Смена пароля

    context = {'recipes_list': recipes_list,
               'recipe_form': recipe_form,
               'cp_form': cp_form,
               'favorite_list': favorite_list,
              }
    return render(request, 'studentfood/html/profiles/profile.html', context)


def change_password(request):
    if request.method == 'POST':
        cp_user = request.user
        cp_form = ChangePasswordForm(request.POST)
        if cp_form.is_valid():
            cp_user.set_password(cp_form.cleaned_data.get("password"))
            cp_user.save()
    return redirect('studentfood:main')