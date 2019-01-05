from django.urls import path , re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='movie2'

urlpatterns = [

    path('listofposts', views.listofposts, name='listofposts'),
    
   

   ]