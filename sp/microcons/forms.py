from django import forms

class MicroConsForm(forms.Form):
	
	thesis = forms.CharField(
		max_length=130,
		help_text=u"Enter your idea in 140 characters or less.")
	
	majority = forms.CharField(max_length=3)
	
	prop_hours = forms.CharField(max_length=3)
	
	firstcontent = forms.CharField(widget=forms.Textarea)