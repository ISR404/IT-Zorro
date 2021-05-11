from django import forms
from .models import User, Recipe
from django.db import models


class CommentForm(forms.Form):
    text = forms.CharField(help_text='Текст комментария', max_length=1500)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ("recipe_name", "description", "price", "category", "photo")


