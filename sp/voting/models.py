from django.db import models
from django.forms import ModelForm

class Vote_Counter(models.Model):
	prop_id = models.IntegerField()
	vote_for = models.IntegerField()
	vote_against = models.IntegerField()
	percentage_for = models.IntegerField()
	threshold = models.IntegerField()
	current_status = models.TextField()
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Vote_Records(models.Model):
	user_id = models.IntegerField()
	createtime = models.DateTimeField(auto_now_add=True)
	target_prop = models.IntegerField()
	for_against = models.IntegerField()
