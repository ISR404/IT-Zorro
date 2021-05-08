from django import forms
from .models import User, Recipe
from django.db import models


class CommentForm(forms.Form):
    text = forms.CharField(help_text='Текст комментария', max_length=1500)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ("recipe_name", "description", "price", "category", "photo")
    """recipe_name = forms.CharField(help_text='Название рецепта', max_length=40)
    description = forms.CharField(help_text='Описание рецепта', widget=forms.Textarea)
    category = forms.ChoiceField(help_text='Категория рецепта', choices=Recipe.GLOBAL_CATEGORY)
    price = forms.IntegerField(help_text='Примерная стоимость', required=False)"""

