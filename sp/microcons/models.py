from django.db import models
from django.forms import ModelForm
from django import forms

class MicroCons(models.Model):
	thesis = models.CharField(max_length=100)
	articlecontent = models.TextField()
	majority = models.IntegerField(max_length=3)
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s" % (self.thesis)

	class Meta:
		verbose_name_plural = "Micro-constitutions"

class MicroConsModelForm(ModelForm):
	class Meta:
		model = MicroCons

