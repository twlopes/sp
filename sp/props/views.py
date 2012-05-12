from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.props.models import Props
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.props.diff_match_patch import *

def edit_article(request, articleid):
	errors = []

	if request.method == 'POST':
		dfunction = diff_match_patch()
				
		# formatinitialtext
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		formatted = data.encode("utf8")

		form = PropForm(request.POST)
		if form.is_valid():
			
			data = form.cleaned_data['article']
			asciidata = data.encode("utf8")
			diff = dfunction.diff_main(formatted, asciidata)
			diffhtml = dfunction.diff_prettyHtml(diff)
			p = Props(idversions=articleid, maindiff=diff, patch=diff, htmldiff=diffhtml)
			p.save()
		
		return render_to_response('donediff.html', {'diff': diffhtml})

	else:
		
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		initial = data.encode("utf8")
		
		
		populate = MicroCons.objects.get(id__contains=articleid)
		form = PropForm(initial={'article': initial})

	return render_to_response('editarticle.html', {'form': form})