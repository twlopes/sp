from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from sp.microcons.models import MicroCons, MicroConsModelForm
from sp.props.models import Props
from django.http import HttpResponse, HttpResponseRedirect

def latest_articles(request):
	article = (MicroCons.objects.order_by('createtime').reverse())[:5]
	return render_to_response ('latest_articles.html', {'article': article}, context_instance=RequestContext(request))

def view_article(request, articleid):
	article = MicroCons.objects.get(id__contains=articleid)

	data = MicroCons.objects.get(id__contains=articleid).articlecontent
	articlecontent_data = data.encode("utf8")

	prop_data = Props.objects.get(microcons_id__contains=articleid)
	
	try:
		prop = Props.objects.get(id=articleid)
	except Props.DoesNotExist:
		prop = None

	return render_to_response(
		'article_view.html', 
		{
		'article': article, 
		'articlecontent_data': articlecontent_data, 
		'articleid': articleid,
		'prop_data':prop_data
		}, 
		context_instance=RequestContext(request)
		)