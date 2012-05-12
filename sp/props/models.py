from django.db import models
from django.forms import ModelForm
from sp.microcons.models import MicroCons

class Props(models.Model):
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	idversions = models.IntegerField(editable=False)
	maindiff = models.TextField(editable=False) 
	patch = models.TextField(editable=False)
	htmldiff = models.TextField(editable=False)
		
	def __unicode__(self):
		return self.thesis