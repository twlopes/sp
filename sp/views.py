from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
from celery.task import task
from django.template import loader, RequestContext
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from sp.props.models import Props
from django.contrib.auth.models import User, Permission, Group
from follow.models import Follow
from sp.microcons.models import MicroCons
import itertools

def insta_links(request):
	return render_to_response('insta_links.html', context_instance=RequestContext(request))

@login_required
def home(request):

	# name of current user
	person = request.user
	
	# Grab user object
	user_set = User.objects.get(username=person)
	
	# grab user id from object
	user_number = user_set.id

	# query set to grab articles/microcons that the user is following
	q_set = Follow.objects.filter(user_id=user_number).values_list('target_microcons_id')
	
	# formatting data
	result = map(list, q_set)
	next=sum(result, [])

	# building list of props for constitutions that user is following.
	elements=[]
	for i in next:
		results=Props.objects.filter(microcons_id=i)
		elements.append(results)

	# chain together lists of lists (which are results)
	props=list(itertools.chain.from_iterable(elements))

	return  render_to_response('home.html', {'person': person, 'props': props,}, context_instance=RequestContext(request))