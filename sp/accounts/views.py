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

# def login_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Correct password, and the user is marked "active"
#         auth.login(request, user)
#         # Redirect to a success page.
#         return HttpResponseRedirect("/login_page/")
#     else:
#         # Show an error page
#         return HttpResponseRedirect("/user_home/")

def register_done(request):
	return render_to_response('register_done.html')
	
def user_home(request):
	return render_to_response('user_home.html', {'user':user})