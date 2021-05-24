from django import forms
from .models import User, Recipe,Comment
from django.db import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ("recipe_name", "description", "price", "category", "photo")