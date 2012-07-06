from django.db import models
from django.forms import ModelForm, Textarea, DateField, CharField
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
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


class MicroConsModelForm(forms.ModelForm):
	
	class Meta:
		model = MicroCons


	thesis = forms.CharField(
		label = 'Thesis',
		required = 'True',
		widget = forms.Textarea(),


	)

	articlecontent = forms.CharField(
		label = 'Article Content',
		required = 'True',
	)

	majority = forms.CharField(
		label = 'Majority',
		required = 'True',
	)

	prop_hours = forms.CharField(
		label = 'Prop Hours',
		required = 'True',
	)

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		# self.helper.form_class = "message"
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Submit'))


		self.helper.layout=Layout(
    			Field('thesis', css_class="message"),
    			Fieldset(
        			# 'Tell us your favorite stuff {{ username }}',
        			
        			'articlecontent',
        			HTML("""<span class="countdown"></span><p>"""),
        			

        			
        			# 'prop_hours',
        			# 'majority',
        			
    			)
			)
		super(MicroConsModelForm, self).__init__(*args, **kwargs)

	
        