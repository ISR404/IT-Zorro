from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    #path('catalog/', views.index, name='index'),
    #path('<int:recipe_id>/', views.detail, name='detail'),
    path('', views.mainpage, name='main'),
    path('register/', views.register, name='register'),
    path('authoriz/', views.authoriz, name='authoriz'),
    path('product', views.product, name='product'),
    path('profile/', views.profile, name='profile'),
]