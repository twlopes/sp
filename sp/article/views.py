from __future__ import division
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from sp.microcons.models import MicroCons, MicroConsModelForm
from sp.props.models import Props
from follow import models
from sp.article.models import Articles
from django.http import HttpResponse, HttpResponseRedirect
from follow.models import Follow


def view_article(request, articleid):
	
	article = MicroCons.objects.get(id__contains=articleid)

	data_one = (Articles.objects.filter(cons_id=articleid).order_by('version_id').reverse())[:1]
	data=data_one[0]
	
	# articlecontent_data = data.encode("utf8")
	prop_data = Props.objects.filter(microcons_id=articleid).filter(currency = "expired").filter(pass_status="pass").order_by('createtime').reverse()[:5]
	
	# Query for number of followers
	follower_number=Follow.objects.get_follows(MicroCons.objects.filter(id=articleid)).count()

	# total number of props
	total = Props.objects.filter(cons_id_key_id=articleid).count()

	# Query for accepted props
	accepted_props=Props.objects.filter(cons_id_key_id=articleid).filter(success="yes").count()

	# Query for props outstanding
	outstanding = Props.objects.filter(cons_id_key_id=articleid).filter(success="undetermined").count()

	# Query and calculation for acceptance rate.
	total_props = Props.objects.filter(cons_id_key_id=articleid).filter(currency="expired").count()
	
	if total_props == 0:
		percentage_accepted = "No props have run their course yet!"
	elif accepted_props == 0:
		percentage_accepted = "No props have been accepted yet!"
	else:
		number = accepted_props / total_props * 100
		percentage_accepted = "%d percent of props have been accepted." % number

	return render_to_response(
		'article_view.html', 
		{
		'total': total,
		'article': article, 
		'data': data, 
		'percentage_accepted': percentage_accepted,
		'articleid': articleid,
		'outstanding': outstanding,
		'prop_data': prop_data,
		'follower_number': follower_number,
		'accepted_props': accepted_props,
		}, 
		context_instance=RequestContext(request)
		)