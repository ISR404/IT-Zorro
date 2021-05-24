from django.urls import path

from IT_Zorro import settings
from . import views
from django.conf.urls.static import static

app_name = 'studentfood'
urlpatterns = [
    path('catalog/', views.main, name='main'),
    path('detail/<int:recipe_id>', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)