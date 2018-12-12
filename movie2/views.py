from django.shortcuts import render
from movie2.models import Posts




def listofposts(request):
    post=Posts.objects.all().order_by('published')
    arg={'post':post}
    return render(request , 'movie2/listofposts.html', arg)

# Create your views here.
