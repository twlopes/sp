from django import forms

class PropForm(forms.Form):
	article = forms.CharField(widget=forms.Textarea)


