from django.contrib import admin
from .models import User, Recipe, Comment, Mark, BookMark

# Register your models here.

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Mark)
admin.site.register(BookMark)
