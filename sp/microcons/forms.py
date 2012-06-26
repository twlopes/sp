from django import forms

class MicroConsForm(forms.Form):
	thesis = forms.CharField(max_length=130)
	majority = forms.CharField(max_length=3)
	prop_hours = forms.CharField(max_length=3)
	firstcontent = forms.CharField(widget=forms.Textarea)