from django.db import models
from django.forms import ModelForm

class Vote(models.Model):
	prop_id = models.IntegerField()
	vote_for = models.IntegerField()
	vote_against = models.IntegerField()
	percentage_for = models.IntegerField()
	threshold = models.IntegerField()
	current_status = models.TextField()
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# 
	# class Meta:
	# 	app_label =  'voting'