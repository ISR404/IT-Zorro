from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Recipe, User, Comment
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login



# Create your views here.

def index(request):
    recipes_list = Recipe.objects.order_by('-pub_date')
    context = {'recipes_list': recipes_list}
    return render(request, 'studentfood/backend-temp/test_schema.html', context)


def detail(request, recipe_id):
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'studentfood/backend-temp/detail_test.html', {'recipe_detail': recipe_detail})

def mainpage(request):
    return render(request, 'studentfood/main.html')

def register(request):
    return render(request, 'profiles/register.html')

def authoriz(request):
    return render(request, '')

def product(request):
    return render(request, 'studentfood/product.html')

def profile(request):
    return render(request, 'profiles/profile.html')