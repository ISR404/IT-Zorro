from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, User, Comment


# Create your views here.

def index(request):
    recipes_list = Recipe.objects.all()
    output = ', '.join([r.recipe_name for r in recipes_list])
    return HttpResponse(output)
