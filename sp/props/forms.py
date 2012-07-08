from django import forms

class PropForm(forms.Form):
	article = forms.CharField(
		label = '',
		widget=forms.Textarea(attrs={'class':'span7'}),
	)