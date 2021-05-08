from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    path('catalog/', views.main, name='main'),
    path('detail/<int:recipe_id>', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('profile/', views.profile, name='profile'),
]