from celery.task import task
from datetime import datetime, timedelta
from celery.task import task
from sp.props.models import Props
from sp.microcons.models import MicroCons
from django.db import models
from django.forms import ModelForm
from sp.props.diff_match_patch import *

# function to save to database

@task
def expiry(z):
	
	# Get prop record
	record = Props.objects.get(id=z)

	# Get article number
	article_number = record.microcons_id
	
	# Save into object instance.
	record.currency = "expired"
	
	# Send back into database.
	record.save()
	
	# Get article record
	article = MicroCons.objects.get(id=article_number)

	if record.pass_status == "pass":
		dfunction = diff_match_patch()
		patch = record.patch
		content = article.articlecontent
		result = dfunction.patch_apply(patch, content)
		
		article.articlecontent = result[0]

		article.save()

	else:
		pass





@task
def time_expiry(next, hours):
	record = Props.objects.get(id=next)
	record.currency = "expired"
	record.save()
