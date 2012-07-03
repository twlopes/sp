from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from sp.microcons.models import MicroCons, MicroConsModelForm
from sp.props.models import Props
from django.http import HttpResponse, HttpResponseRedirect

def latest_articles(request):
	article = (MicroCons.objects.order_by('createtime').reverse())[:5]
	return render_to_response ('latest.html', {'article': article}, context_instance=RequestContext(request))

def view_article(request, articleid):
	article = MicroCons.objects.filter(id__contains=articleid)
	htmldiff = Props.objects.filter(microcons_id__contains=articleid)
	try:
		prop = Props.objects.get(id=articleid)
	except Props.DoesNotExist:
		prop = None
	return render_to_response('articleview.html', {'article': article, 'articleid': articleid, 'displaydiff': htmldiff, 'prop':prop}, context_instance=RequestContext(request))