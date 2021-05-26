from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:recipe_id>/', views.detail, name='detail'),
    path('profile/', views.profile, name='profile'),
    path('favourite_added/<int:recipe_id>/', views.favourite_add, name='favourite_add'),
    path('password_reset', views.change_password, name='password_reset'),
    path('change_photo/', views.change_photo, name='change_photo')
]