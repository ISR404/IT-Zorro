from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, User, Comment


# Create your views here.

def index(request):
    recipes_list = Recipe.objects.order_by('-pub_date')[:5]
    output = ', '.join([r.recipe_name for r in recipes_list])
    return HttpResponse(output)


def detail(request, recipe_id):
    response = "Вы открыли рецепт с индексом %s"
    return HttpResponse(response % recipe_id)