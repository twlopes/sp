from django.db import models
from django.forms import ModelForm

class Edits(models.Model):
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	diffnotation = models.TextField(blank=True)
		
	def __unicode__(self):
		return self.thesis

class EditsForm(ModelForm):
	class Meta:
		model = Edits