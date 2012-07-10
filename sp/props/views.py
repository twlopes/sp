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
import re


@login_required
def create_prop(request, articleid):
	if request.method == 'POST':
		dfunction = diff_match_patch()
				
		# Creating version to be amended to run diff against.
		
		first = MicroCons.objects.get(id__contains=articleid)
		data = first.articlecontent
		hours_number = first.prop_hours
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
			
			# Processing diff into different lengths.

			match_list = re.findall('(\S*.{50}<[id][ne][sl] style="background.*">.*<\W[di][en][ls]>.{50}\S*)', diffhtml)
			long_diffo = '</br></br>'.join(match_list)

			# Saving diff results to database.
			
			p = Props(microcons_id=articleid, expiry_time=time_object, current_status="current", maindiff=diff, 
				long_diff=long_diffo, patch=patchdata, htmldiff=diffhtml)
			
			p.save()
			next = p.id

			# Programming the expiry of the prop.
			
			expiry.apply_async(args=[next], eta=time_object)

			# Getting prop details so that vote entry can be created.
			
			x = Props.objects.filter(id=next).values()
			data = x[0]
			z = data['id']
			
			# Getting constitution voting threshold so that vote entry can be created.
			
			q = MicroCons.objects.get(id__contains=articleid)
			r = q.majority

			# Saving initial record in voting table.
			
			q = Vote(prop_id=z, vote_for=0, vote_against=0, percentage_for=0, threshold=r, current_status="current")
			q.save()
		
		return render_to_response('prop_confirm.html', {'diff': diffhtml, 'time_object': time_object, 
			'hours_number': hours_number, 'micro_cons': r}, context_instance=RequestContext(request))

	else:
		
		# Put together initial data for the form.
		
		first = MicroCons.objects.get(id__contains=articleid).articlecontent
		initial = first.encode("utf8")
		thesis = MicroCons.objects.get(id__contains=articleid).thesis
		
		# Displaying initial data in form.
		
		populate = MicroCons.objects.get(id=articleid)
		form = PropForm(initial={'article': initial})

	return render_to_response('editarticle.html', {'form': form, 'thesis': thesis}, context_instance=RequestContext(request))

def view_article_props(request, articleid):
	htmldiff = Props.objects.filter(microcons_id__contains=articleid)
	try:
		prop = Props.objects.get(id=articleid)
	except Props.DoesNotExist:
		prop = None
	return render_to_response('articleprops.html', {'articleid': articleid, 'displaydiff': htmldiff, 'prop':prop}, context_instance=RequestContext(request))

def view_single_prop(request, propid):
	prop = Props.objects.get(id=propid)
	longdiff = Props.objects.get(id=propid).long_diff
	return render_to_response('singleprop.html', {'prop':prop, 'propid':propid, 'longdiff':longdiff}, context_instance=RequestContext(request))

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