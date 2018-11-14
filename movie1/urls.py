from django.urls import path , re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='movie1'
urlpatterns = [
    path('',views.index, name='index'),
    path('cricket', views.cric, name='cric'),
    path('football', views.football, name='football'),
    path('vollyball', views.vollyball, name='vollyball'),
    path('listofposts', views.listofposts, name='listofposts'),
    path('facebook', views.facebook, name='facebook'),

    re_path('(?P<slug>[\W-]+)/$' ,  views.posts_detail, name='postsdetail'),


]



