from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.versions.models import EditForm
from sp.microcons.models import MicroConsModelForm, MicroCons

# def view_article(request, articleid):
# 	article = MicroCons.objects.filter(id__contains=articleid)
# 	return render_to_response('articleview.html', {'article': article})


def edit_article(request, articleid):
	populatecontent = MicroCons.objects.get(id__contains=articleid)
	errors = []
	if request.method == 'POST':
		form = EditForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/done/')
	else:
		form = EditForm(
			initial={'markup': populatecontent}
			)
	return render_to_response('editarticle.html', {'form': form})