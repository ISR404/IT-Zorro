from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'studentfood'
urlpatterns = [
    path('', views.main, name='main'),
    url(r'^detail/([0-9]{1,3})/$', views.detail, name='detail'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^favourite_added/([0-9]{1,3})/$', views.favourite_add, name='favourite_add'),
    url(r'^password_reset/$', views.change_password, name='password_reset'),
    url(r'^change_photo/$', views.change_photo, name='change_photo'),
    url(r'^remove_recipe/([0-9]{1,3})/$', views.remove_recipe, name='remove_recipe'),
]
