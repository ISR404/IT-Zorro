from django import forms
from .models import User, Recipe


class CommentForm(forms.Form):
    text = forms.CharField(help_text='Текст комментария', max_length=1500)
