from django import forms

class PropForm(forms.Form):
	article = forms.CharField(
		label = '',
		widget=forms.Textarea(attrs={'id':'demo1', 'class':'span7', 'rows':'20'}),
	)