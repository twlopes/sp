from django.db import models
from django.forms import ModelForm
from sp.microcons.models import MicroCons

class Props(models.Model):
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	idversions = models.IntegerField()
	maindiff = models.TextField() 
	patch = models.TextField()
	htmldiff = models.TextField()

	def __unicode__(self):
		return self.maindiff
	
	class Meta:
		verbose_name_plural = "Propositions"