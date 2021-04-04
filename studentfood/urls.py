from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    path('catalog/', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail')
]