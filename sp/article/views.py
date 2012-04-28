from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from django.template.loader import get_template
from sp.microcons.models import MicroCons
from django.http import HttpResponse, HttpResponseRedirect
from sp.microcons.models import MicroConsModelForm


def latest_articles(request):
	article = (MicroCons.objects.order_by('createtime').reverse())[:5]
	return render_to_response ('latest.html', {'article': article})

def view_article(request, articleid):
	# articleid = int(articleid)
	article = MicroCons.objects.filter(id__contains=articleid)
	return render_to_response('articleview.html', {'article': article})

def view_article(request, articleid):
	# articleid = int(articleid)
	article = MicroCons.objects.filter(id__contains=articleid)
	return render_to_response('articleview.html', {'article': article})