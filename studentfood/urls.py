from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    path('catalog/', views.main, name='main'),
    path('detail/', views.detail, name='detail'),
    # path('product', views.product, name='product'),
    path('profile/', views.profile, name='profile'),
]