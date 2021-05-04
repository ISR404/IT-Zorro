from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, User, Comment
from django.http import Http404
from .forms import CommentForm


# Create your views here.

def main(request, use_filter=''):  # лист рецептов,
    null_recipe = Recipe()
    raw_category = null_recipe.GLOBAL_CATEGORY
    site_category = []
    first_arg = []
    for elem in raw_category:
        site_category.append(elem[1])
        first_arg.append(elem[0])
    if use_filter == '':
        recipes_list = Recipe.objects.order_by('-pub_date')
    else:
        recipes_list = Recipe.objects.get(category__iexact=use_filter)
    context = {'recipes_list': recipes_list,
               'site_category': site_category,
               'first_arg': first_arg,
               'raw_category': raw_category
               }
    return render(request, 'studentfood/html/main.html', context)


def detail(request, recipe_id):  # объект (написать список полей)
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    comment_list = Comment.objects.order_by('pub_date')
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
                                                             'comment_form': comment_form,
                                                             'comment_list': comment_list})


def register(request):  # реализация Димы
    return render(request, 'profiles/register.html')


def profile(request):  # пользовательские данные (при переходе возвращает объект пользователя)
    return render(request, 'profiles/profile.html')


def category_filter(request):
    pass


