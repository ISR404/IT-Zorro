from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Recipe, User, Comment
from django.http import Http404


# Create your views here.

def main(request): # лист рецептов,
    recipes_list = Recipe.objects.order_by('-pub_date')
    null_recipe = Recipe()
    raw_category = null_recipe.GLOBAL_CATEGORY
    site_category = []
    first = Recipe.objects.filter(category='Первые блюда')
    second = Recipe.objects.filter(category='Вторые блюда')
    for elem in raw_category:
        site_category.append(elem[1])
    context = {'recipes_list': recipes_list,
               'site_category': site_category,
               'first': first,
               'second': second
              }
    return render(request, 'studentfood/html/main.html', context)


def detail(request, recipe_id):  # объект (написать список полей)
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'studentfood/html/product.html', {'recipe_detail': recipe_detail})


def profile(request):  # пользовательские данные (при переходе возвращает объект пользователя)
    return render(request, 'studentfood/html/profiles/profile.html')


def category_filter(request):
    pass
