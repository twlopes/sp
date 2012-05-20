from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse

def insta_links(request):
	return render_to_response('insta_links.html')
