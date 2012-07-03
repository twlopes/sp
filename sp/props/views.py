from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from sp.props.models import Props
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.props.diff_match_patch import *
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from sp.voting.models import Vote
from sp.tasks import expiry


@login_required
def create_prop(request, articleid):
	if request.method == 'POST':
		dfunction = diff_match_patch()
				
		# Creating version to be amended to run diff against.
		
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		hours_number = valuelist['prop_hours']
		formatted = data.encode("utf8")

		form = PropForm(request.POST)
		if form.is_valid():
			
			# Running diff functions and creating entries.
			
			data = form.cleaned_data['article']
			asciidata = data.encode("utf8")
			diff = dfunction.diff_main(formatted, asciidata)
			diffhtml = dfunction.diff_prettyHtml(diff)
			
			patchdata = dfunction.patch_make(formatted, asciidata)

			time_object = datetime.now() + timedelta(minutes=hours_number)
			
			# Saving diff results to database.
			
			p = Props(microcons_id=articleid, expiry_time=time_object, current_status="current", maindiff=diff, patch=patchdata, htmldiff=diffhtml)
			p.save()
			next = p.id
			
			# Programming the expiry of the prop.
			
			expiry.apply_async(args=[next], eta=time_object)

			# Getting prop details so that vote entry can be created.
			
			x = Props.objects.filter(id=next).values()
			data = x[0]
			z = data['id']
			
			# Getting constitution voting threshold so that vote entry can be created.
			
			threshold_data = MicroCons.objects.filter(id__contains=articleid).values()
			y = threshold_data[0]
			q = y['majority']
				
			# Saving initial record in voting table.
			
			q = Vote(prop_id=z, vote_for=0, vote_against=0, percentage_for=0, threshold=q, current_status="current")
			q.save()
		
		return render_to_response('donediff.html', {'diff': diffhtml}, context_instance=RequestContext(request))

	else:
		
		# Put together initial data for the form.
		
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		initial = data.encode("utf8")
		
		# Displaying initial data in form.
		
		populate = MicroCons.objects.get(id=articleid)
		form = PropForm(initial={'article': initial})

	return render_to_response('editarticle.html', {'form': form}, context_instance=RequestContext(request))

def view_article_props(request, articleid):
	htmldiff = Props.objects.filter(microcons_id__contains=articleid)
	try:
		prop = Props.objects.get(id=articleid)
	except Props.DoesNotExist:
		prop = None
	return render_to_response('articleprops.html', {'articleid': articleid, 'displaydiff': htmldiff, 'prop':prop}, context_instance=RequestContext(request))

def view_single_prop(request, propid):
	prop = Props.objects.get(id=propid)
	return render_to_response('singleprop.html', {'prop':prop, 'propid':propid}, context_instance=RequestContext(request))

def view_latest_props(request):
	prop = (Props.objects.order_by('createtime').reverse())[:5]
	return render_to_response('latestprops.html', {'prop':prop}, context_instance=RequestContext(request))

def prop_accept(request, propid):
	
	prop_record = Props.objects.get(id=propid)

	dfunction = diff_match_patch()
	articleid = prop_record.microcons_id
	patch = prop_record.patch

	article_record = MicroCons.objects.get(id=articleid)

	articlecontent = article_record.articlecontent
	
	article_record = MicroCons.objects.get(id=articleid)
	prop_text = article_record.articlecontent.encode("utf8")
	
	result = dfunction.patch_apply(patch, prop_text)
	newcontent = result[0]
	
	MicroCons.objects.filter(id=articleid).update(articlecontent=newcontent)
	
	return render_to_response('done.html', context_instance=RequestContext(request))