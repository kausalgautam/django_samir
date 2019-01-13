from django.shortcuts import render , redirect

from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
	if request.method== 'POST':
		forms=UserRegisterForm(request.POST)
		if forms.is_valid():
			forms.save()
			username=forms.cleaned_data.get('username')
			messages.success(request, f'Account Created for {username}!')
			



	else:
		forms=UserRegisterForm()
	return render(request, 'users/register.html' , {'form':forms})
