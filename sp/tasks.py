from celery.task import task
from datetime import datetime, timedelta
from celery.task import task
from sp.props.models import Props
from sp.microcons.models import MicroCons
from django.db import models
from django.forms import ModelForm
from sp.props.diff_match_patch import *
from sp.article.models import Articles

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

		qset = (Articles.objects.filter(cons_id=article_number).order_by('version_id').reverse())[:1]
		q = qset[0]
		content = q.articlecontent
		previous_version_id = q.version_id
		new_version_id = previous_version_id + 1

		patched_content = dfunction.patch_apply(patch, content)
		
		# Gets the new content and leaves out the result.

		formatted_content = patched_content[0]
		
		# creating the new record to be saved.

		n = Articles(
			cons_id = article_number,
			version_id=new_version_id,
			articlecontent=formatted_content,
			)

		# Ensures a new row, not an amendment to old row.

		n.pk = None
		n.save()

	else:
		pass

@task
def time_expiry(next, hours):
	record = Props.objects.get(id=next)
	record.currency = "expired"
	record.save()
