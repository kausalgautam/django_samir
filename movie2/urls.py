from django.urls import path , re_path
from  .views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='movie2'


urlpatterns = [
        path('blog/list/',BlogListView.as_view(), name="bloglist"),
        path('blog/<int:pk>/detail/',BlogDetailView.as_view(), name="blogdetail"),
        path('blog/create/', BlogCreateView.as_view(), name="blogcreate"),
        path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name="blogupdate"),
        path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name="blogdelete"), #some particular 1 data sp using pk

 
 
]