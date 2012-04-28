from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse

def home_page(request):
	return render_to_response('home_page.html')
