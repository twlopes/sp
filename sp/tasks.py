from celery.task import task
from datetime import datetime, timedelta
from celery.task import task
from sp.props.models import Props
from django.db import models
from django.forms import ModelForm

# function to save to database

@task
def expiry(z):
	record = Props.objects.get(id=z)
	
	# Save into object instance.
	
	record.currency = "expired"
	
	# Send back into database.

	record.save()
	
	# return z + y


@task
def time_expiry(next, hours):
	record = Props.objects.get(id=next)
	record.currency = "expired"
	record.save()
