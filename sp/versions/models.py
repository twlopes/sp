from django.db import models
from django.forms import ModelForm

class Edits(models.Model):
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	markup = models.TextField()
	
	def __unicode__(self):
		return self.thesis

class EditForm(ModelForm):
	class Meta:
		model = Edits