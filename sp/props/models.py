from django.db import models
from django.forms import ModelForm
from sp.microcons.models import MicroCons
from picklefield.fields import PickledObjectField

class Props(models.Model):
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	microcons_id = models.IntegerField()
	author = models.TextField()
	maindiff = PickledObjectField()
	short_diff = models.TextField()
	medium_diff = models.TextField()
	long_diff = models.TextField()
	patch = PickledObjectField()
	htmldiff = models.TextField()
	expiry_time = models.DateTimeField()
	currency = models.TextField()
	vote_for = models.IntegerField()
	vote_against = models.IntegerField()
	percentage_for = models.IntegerField()
	threshold = models.IntegerField()
	pass_status = models.TextField()
	
	# def __unicode__(self):
	# 	return self.htmldiff
	
	class Meta:
		verbose_name_plural = "Propositions"

		# Made changes to model in commmit before