from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.versions.models import Edits
from sp.versions.forms import EditForm
from sp.microcons.models import MicroCons
from sp.versions.diff_match_patch import *

def edit_article(request, articleid):
	errors = []

	if request.method == 'POST':
		dfunction = diff_match_patch()
				
		# formatinitialtext
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		formatted = data.encode("utf8")

		form = EditForm(request.POST)
		if form.is_valid():
			
			data = form.cleaned_data['article']
			asciidata = data.encode("utf8")

			diff = dfunction.diff_main(formatted, asciidata)
			
			diffhtml = dfunction.diff_prettyHtml(diff)
			
			p = Edits(idversions=articleid, patch=diff, htmldiff=diffhtml)
			p.save()
		
		return render_to_response('donediff.html', {'diff': diffhtml})

	else:
		populate = MicroCons.objects.get(id__contains=articleid)
		form = EditForm(initial={'article': populate})
	return render_to_response('editarticle.html', {'form': form})