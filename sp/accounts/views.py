from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def login_page(request):
	return render_to_response('login.html')	

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/register_done/')
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form,
    })

def register_done(request):
	return render_to_response('register_done.html')
	
def user_home(request):
	return render_to_response('user_home.html', {'user':user})
	
def profile(request):
	return render_to_response('profile.html')