from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name='users'
urlpatterns= [
 path('register', views.register, name='register'),
]