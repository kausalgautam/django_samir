from django.shortcuts import HttpResponse, render_to_response
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






def facebook(request):

    nameo="kausal111"
    argh={'name':nameo}
    return render(request , 'movie1/facebook.html' , argh)











