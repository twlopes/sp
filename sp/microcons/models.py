from django.db import models
from follow import utils
from django.forms import ModelForm, Textarea, DateField, CharField
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from django.contrib.auth.models import User

class MicroCons(models.Model):
	thesis = models.CharField(max_length=100)
	director = models.ForeignKey(User)
	majority = models.IntegerField(max_length=3)
	prop_hours = models.IntegerField(max_length=3)
	createtime = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s" % (self.thesis)

	class Meta:
		verbose_name_plural = "Micro-constitutions"

# registers the model with follow app

utils.register(MicroCons)

class MicroConsModelForm(forms.ModelForm):
	
	class Meta:
		model = MicroCons
		exclude = ('director')

	thesis = forms.CharField(
		label = 'Thesis',
		required = 'True',
		help_text = "What's your opinion in 130 characters or less.  Make it the kernel of your idea.  Short and sweet.",
		widget = forms.Textarea(attrs={'rows':'2'}),
	)

	majority = forms.CharField(
		label = 'Majority',
		required = 'True',
		help_text = 'This is the threshold of votes required to pass content into the article.',

	)

	prop_hours = forms.CharField(
		label = 'Prop Hours',
		required = 'True',
		help_text = 'How many hours do you want to give people to vote?',
		# widget = forms.TextInput(attrs={'class':'span2'}),
	)

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.layout=Layout(
    			HTML("""<div class="span 3 offset6"><span class="countdown"></span></div></br>"""),
    			Field('thesis', css_class="message span6 input-xlarge"),
    			HTML("""</br>"""),
    			HTML("""</br>"""),
    			AppendedText('majority', '%'),
    			AppendedText('prop_hours', 'Hours', 'span1'),
				# FormActions(
				# 	# Submit('save_changes', 'Submit', css_class="btn-primary")
				# 	)			
			)
		super(MicroConsModelForm, self).__init__(*args, **kwargs)

	
        