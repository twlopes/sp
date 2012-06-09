from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
from celery.task import task

def insta_links(request):
	return render_to_response('insta_links.html')

@task
def addo(x, y):
	return x + y
