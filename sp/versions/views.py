from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.versions.models import EditForm
from sp.microcons.models import MicroConsModelForm, MicroCons

# def view_article(request, articleid):
# 	article = MicroCons.objects.filter(id__contains=articleid)
# 	return render_to_response('articleview.html', {'article': article})


def edit_article(request, articleid):
	contentdisplay = [p.articlecontent for p in MicroCons.objects.filter(id__contains=articleid)]
	# articleid = MicroCons.objects.all
	errors = []
	if request.method == 'POST':
		form = EditForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/done/')
	else:
		form = EditForm(
			initial={'markup': contentdisplay}
			)
	return render_to_response('editarticle.html', {'form': form})
