from django.views.generic import *
from  movie2.models import *
from  movie2.forms import *



class BlogListView(ListView):
	template_name = "bloglist.html"
	model = Blog #we may have othe datatable so  speciang here.
	context_object_name = "blogs" # sending data from view to template with name bogs


class BlogDetailView(DetailView):
	template_name = "blogdetail.html"
	model = Blog #we may have othe datatable so  speciang here.
	context_object_name = "blogdetail" # sending data from view to template with name bogs


class BlogCreateView(CreateView):
	template_name = "blogcreate.html"
	form_class =BlogForm
	success_url='/movie2/blog/list/'


class BlogUpdateView(UpdateView):
	template_name = "blogcreate.html"
	model= Blog
	form_class =BlogForm
	success_url='/movie2/blog/list/'


class BlogDeleteView(DeleteView):
	template_name = "blogdelete.html"
	model= Blog
	success_url='/movie2/blog/list/'



# Create your views here.
