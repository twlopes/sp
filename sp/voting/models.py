from django.db import models
from django.forms import ModelForm

class Vote_Records(models.Model):
	user_id = models.IntegerField()
	createtime = models.DateTimeField(auto_now_add=True)
	target_prop = models.IntegerField()
	for_against = models.TextField()
