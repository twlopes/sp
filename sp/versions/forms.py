from django import forms

class EditForm(forms.Form):
	firstcontent = forms.CharField(widget=forms.Textarea)