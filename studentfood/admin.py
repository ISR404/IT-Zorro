from django.contrib import admin
from .models import User, Recipe, Comment, Mark

# Register your models here.

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Mark)