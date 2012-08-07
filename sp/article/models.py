from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, DateField, CharField
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from sp.microcons.models import MicroCons
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset


class Articles(models.Model):
	createtime = models.DateTimeField(auto_now_add=True)
	cons_id = models.IntegerField(max_length=3)
	cons_id_key = models.ForeignKey(MicroCons)
	version_id = models.IntegerField(max_length=3)
	articlecontent = models.TextField()

	class Meta:
		verbose_name_plural = "Articles"

class ArticleModelForm(forms.ModelForm):
	
	class Meta:
		model = Articles
		exclude = ('cons_id', 'version_id', 'cons_id_key')

	articlecontent = forms.CharField(
			label = 'Article Content',
			required = 'True',
			widget = forms.Textarea(),
			help_text = 'Put as much article content in as you like.  This will get people started on your idea.',
		)

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.layout=Layout(
    			HTML("""<div class="span 3 offset6"></div>"""),
    			Field('articlecontent', css_class="span6"),
				FormActions(
					Submit('save_changes', 'Submit', css_class="btn-primary")
					)			
			)
		super(ArticleModelForm, self).__init__(*args, **kwargs)