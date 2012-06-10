from celery.task import task
from datetime import datetime, timedelta
from celery.task import task
from sp.voting.models import Vote
from django.db import models
from django.forms import ModelForm

@task
def expiry(z):
	# function to save to database
	record = Vote.objects.get(prop_id=z)
	# Save into object instance.
	record.current_status = "Expired"
	# Send back into database.
	record.save()
	# return z + y