from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, User, Comment


# Create your views here.

def index(request):
    recipes_list = Recipe.objects.order_by('-pub_date')
    context = {'recipes_list': recipes_list}
    return render(request, 'studentfood/backend-temp/test_schema.html', context)


def detail(request, recipe_id):
    recipe_detail = Recipe.objects.get(pk=recipe_id)
    context = {'recipe_detail': recipe_detail}
    return render(request, 'studentfood/backend-temp/detail_test.html', context)
