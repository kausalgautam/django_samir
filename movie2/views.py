from django.shortcuts import render, render_to_response
from movie2.models import Posts




def listofposts(request):
	context = {
	'post': Posts.objects.all().order_by('published')
	}

	return render(request, 'movie2/listofposts.html', context)





	
   
# Create your views here.
