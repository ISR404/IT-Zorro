from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    path('catalog/', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('auth/', views.auth, name='auth'),
    path('product', views.product, name='product'),
    path('profile/', views.profile, name='profile'),
]