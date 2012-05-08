from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.versions.models import Edits, EditsForm
from sp.microcons.models import MicroCons
from sp.versions.diff_match_patch import *

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