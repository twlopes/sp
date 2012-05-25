from django.contrib import auth
from django.template import loader, RequestContext
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# def login_page(request, user):
# 	return HttpResponseRedirect('/accounts/profile/')

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

    }, context_instance=RequestContext(request))

def register_done(request):
	return render_to_response('register_done.html')
	
def profile(request):
	return render_to_response('profile.html', context_instance=RequestContext(request))
	
	# request context gets global variables like user names.