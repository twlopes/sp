from django import forms

class EditForm(forms.Form):
	article = forms.CharField(widget=forms.Textarea)


