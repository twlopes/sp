# from django import forms

# class ArticlesForm(forms.Form):
	
# 	article_content = forms.CharField(
# 		label = 'Article Content',
# 		required = 'True',
# 		widget = forms.Textarea(),
# 		help_text = 'Put as much article content in as you like.  This will get people started on your idea.',
# 	)
	
	# def __init__(self, *args, **kwargs):
	# 	self.helper = FormHelper()
	# 	self.helper.form_method = 'post'
	# 	self.helper.form_class = 'form-horizontal'
	# 	self.helper.layout=Layout(
	# 			HTML("""<div class="span 3 offset6"><span class="countdown"></span></div></br>"""),
	# 			Field('thesis', css_class="message span6 input-xlarge"),
	# 			HTML("""</br>"""),
	# 			Field('articlecontent', css_class="span6"),
	# 			HTML("""</br>"""),
	# 			AppendedText('majority', '%'),
	# 			AppendedText('prop_hours', 'Hours', 'span1'),
	# 			FormActions(
	# 				Submit('save_changes', 'Submit', css_class="btn-primary")
	# 				)			
	# 		)
	# 	super(ArticlesForm, self).__init__(*args, **kwargs)