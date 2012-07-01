from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
from celery.task import task
from django.template import loader, RequestContext
from datetime import datetime, timedelta


def insta_links(request):
	return render_to_response('insta_links.html', context_instance=RequestContext(request))

@task
def addo(x, y):
	return x + y

# from celery.task import task
# >>> from sp.views import addo
# >>> 
# >>> result = addo.apply_async(args=[10, 10], countdown=10)

# The function above runs addo function 10 seconds after.  10, 10 are the numbers that will be added together.


# from celery.task import task
# from datetime import datetime, timedelta
# from celery.task import task
# from sp.voting.models import Vote
# from django.db import models
# from django.forms import ModelForm
# 
# 
# @task
# def expiry(z, x):
# 	# function to save to database
# 	record = Vote.objects.get(prop_id=z)
# 	# Save into object instance.
# 	record.current_status = y
# 	# Send back into database.
# 	record.save()
# 	# return z + y