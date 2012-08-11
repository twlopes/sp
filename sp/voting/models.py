from django.db import models
from django.forms import ModelForm
from sp.props.models import Props

class Vote_Records(models.Model):
	user_id = models.IntegerField()
	createtime = models.DateTimeField(auto_now_add=True)
	target_prop = models.IntegerField()
	prop_id_key = models.ForeignKey(Props)
	for_against = models.TextField()
