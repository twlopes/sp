from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
# from sp.versions.forms import EditForm
from sp.versions.models import Edits
from sp.versions.models import EditsForm
from sp.microcons.models import MicroCons


def edit_article(request, articleid):
	errors = []
	if request.method == 'POST':
		form = EditsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/done/')
	else:
		populatecontent = MicroCons.objects.get(id__contains=articleid)
		form = EditsForm(initial={'diffnotation': populatecontent})
	return render_to_response('editarticle.html', {'form': form})
	
	# initial={'diff': populatecontent}
	
	# cd = form.cleaned_data
	# 			MicroCons.objects.create(diffhtml=cd['Firstcontent'].strip())