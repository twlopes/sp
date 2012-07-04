from django.db import models
from django.forms import ModelForm, Textarea, DateField, CharField
from django import forms
from crispy_forms.bootstrap import AppendedText
from django.contrib.auth.models import User

class MicroCons(models.Model):
	thesis = models.CharField(max_length=100)
	articlecontent = models.TextField()
	director = models.ForeignKey(User)
	majority = models.IntegerField(max_length=3)
	prop_hours = models.IntegerField(max_length=3)
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s" % (self.thesis)

	class Meta:
		verbose_name_plural = "Micro-constitutions"

class MicroConsModelForm(ModelForm):
	thesis = CharField(
		label='Thesis', 
		help_text='The thesis is the kernel of your idea.',
		widget=forms.TextInput(attrs={'class':'message span6'})
		)
	articlecontent = CharField(
		label='Article Content', 
		help_text='Get everyone started on your idea!  Put as much text in here as you like.',
		widget=forms.Textarea(attrs={'class':'span6'})
		)
	majority = CharField(
		label='Voting Majority', 
		help_text='What majority needs to vote for a change for it to pass?',
		widget=forms.TextInput(attrs={'class':'span1'})
		)
	prop_hours = CharField(
		label='Voting Period', 
		help_text='How long will the members have to vote?',
		widget=forms.TextInput(attrs={'class':'span1'})
		)

	class Meta:
		model = MicroCons
		exclude = ('director',)