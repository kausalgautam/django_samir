from django.shortcuts import HttpResponse, render_to_response
from movie1.models import Posts
from django.shortcuts import render,get_object_or_404




def index(request):

    name="kausal"
    args={'name':name}
    return render(request , 'movie1/index.html' , args)

def cric(request):
    message="COMING SOON"

    return render_to_response( 'movie1/cric.html', {"message": message })



def football(request):
    message = "COMING SOON"

    return render_to_response('movie1/football.html', {"message": message})



def vollyball(request):
    message = "COMING SOON"

    return render_to_response('movie1/vollyball.html', {"message": message})


def listofposts(request):
    post=Posts.objects.all().order_by('published')
    arrrg={'post':post}
    return render(request , 'movie1/listofposts.html', arrrg )

def posts_detail(request , slug):

    post=get_object_or_404(Posts , slug=slug)
    return render(request , 'movie1/posts_detail.html' , {'post':post})


def facebook(request):

    nameo="kausal111"
    argh={'name':nameo}
    return render(request , 'movie1/facebook.html' , argh)











