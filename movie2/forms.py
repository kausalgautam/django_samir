from django import forms
from .models import *

class BlogForm(forms.ModelForm):
	class Meta: # done in model form
		model =Blog
		fields = '__all__' 