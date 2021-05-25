from django import forms
from .models import User, Recipe, Comment, Mark
from django.db import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("recipe_name", "description", "price", "category", "photo")


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("password",)


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('mark_value',)


class BookMarkForm(forms.ModelForm):
    check = forms.BooleanField()
