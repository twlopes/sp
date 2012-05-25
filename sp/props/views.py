from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.props.models import Props
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.props.diff_match_patch import *
from django.contrib.auth.decorators import login_required

@login_required
def create_prop(request, articleid):
	
	# form structure
	
	errors = []

	if request.method == 'POST':
		dfunction = diff_match_patch()
				
		# Creating version to be amended to run diff against.
		
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		formatted = data.encode("utf8")

		form = PropForm(request.POST)
		if form.is_valid():
			
			# Running diff functions.
			
			data = form.cleaned_data['article']
			asciidata = data.encode("utf8")
			diff = dfunction.diff_main(formatted, asciidata)
			diffhtml = dfunction.diff_prettyHtml(diff)
			
			patchdata = dfunction.patch_make(formatted, asciidata)
			# Saving diff results to database.
			
			p = Props(idversions=articleid, maindiff=diff, patch=patchdata, htmldiff=diffhtml)
			p.save()
		
		return render_to_response('donediff.html', {'diff': diffhtml})

	else:
		
		# Put together initial data for the form.
		
		first = MicroCons.objects.filter(id__contains=articleid).values()
		valuelist = first[0]
		data = valuelist['articlecontent']
		initial = data.encode("utf8")
		
		# Displaying initial data in form.
		
		populate = MicroCons.objects.get(id=articleid)
		form = PropForm(initial={'article': initial})

	return render_to_response('editarticle.html', {'form': form})

def view_article_props(request, articleid):
	htmldiff = Props.objects.filter(idversions__contains=articleid)
	prop = Props.objects.get(id=articleid)
	return render_to_response('articleprops.html', {'articleid': articleid, 'displaydiff': htmldiff, 'prop':prop})

def view_single_prop(request, propid):
	prop = Props.objects.get(id=propid)
	return render_to_response('singleprop.html', {'prop':prop, 'propid':propid})

def view_latest_props(request):
	prop = (Props.objects.order_by('createtime').reverse())[:5]
	return render_to_response('latestprops.html', {'prop':prop})

def prop_accept(request, propid):
	
	prop_record = Props.objects.get(id=propid)

	dfunction = diff_match_patch()
	articleid = prop_record.idversions
	patch = prop_record.patch

	article_record = MicroCons.objects.get(id=articleid)

	articlecontent = article_record.articlecontent
	
	article_record = MicroCons.objects.get(id=articleid)
	prop_text = article_record.articlecontent.encode("utf8")
	
	result = dfunction.patch_apply(patch, prop_text)
	newcontent = result[0]
	
	MicroCons.objects.filter(id=articleid).update(articlecontent=newcontent)
	
	return render_to_response('done.html')