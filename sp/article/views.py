from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from sp.microcons.models import MicroCons, MicroConsModelForm
from sp.props.models import Props
from sp.article.models import Articles
from django.http import HttpResponse, HttpResponseRedirect

def latest_articles(request):
	article = (MicroCons.objects.order_by('createtime').reverse())[:5]
	return render_to_response ('latest_articles.html', {'article': article}, context_instance=RequestContext(request))

def view_article(request, articleid):
	
	article = MicroCons.objects.get(id__contains=articleid)

	data = Articles.objects.get(cons_id=articleid).articlecontent
	
	# articlecontent_data = data.encode("utf8")

	prop_data = Props.objects.filter(microcons_id=articleid)[:4]
	# .filter(microcons_id__contains=articleid)
	
	return render_to_response(
		'articleview.html', 
		{
		'article': article, 
		'data': data, 
		'articleid': articleid,
		'prop_data': prop_data,
		}, 
		context_instance=RequestContext(request)
		)