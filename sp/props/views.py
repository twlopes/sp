from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from sp.props.models import Props
from sp.article.models import Articles
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.props.diff_match_patch import *
from sp.props.diff_script import long_diff_html

from datetime import datetime, timedelta
from sp.props.models import Props

from django.contrib.auth.decorators import login_required
from sp.tasks import expiry
import re

@login_required
def create_prop(request, articleid):
	if request.method == 'POST':
		
		dfunction = diff_match_patch()
		
		u = request.user

		# Creating version to be amended to run diff against.
		
		first = MicroCons.objects.get(id__contains=articleid)
		content = (Articles.objects.filter(cons_id=articleid).order_by('version_id').reverse())[:1]


		blah = content[0]
		data = blah.articlecontent
		hours_number = first.prop_hours
		r = first.majority
		formatted = data.encode("utf8")

		form = PropForm(request.POST)
		if form.is_valid():
			
			# Running diff functions and creating entries.
			
			data = form.cleaned_data['article']
			utf_data = data.encode("utf8")
			
			# creating callable function for diff

			diff = dfunction.diff_main(formatted, utf_data)
			
			diffhtml = dfunction.diff_prettyHtml(diff)
			patchdata = dfunction.patch_make(formatted, utf_data)

			time_object = datetime.now() + timedelta(minutes=hours_number)
			
			# Processing diff into different lengths.
			
			diff_html_long = long_diff_html(diff)
			
			p = Props(
				microcons_id=articleid,
				cons_id_key=first, 
				author=u,  
				maindiff=diff,
				short_diff="",
				medium_diff="",
				long_diff=diff_html_long, 
				patch=patchdata, 
				htmldiff=diffhtml, 
				expiry_time=time_object,
				currency="current",
				vote_for=0, 
				vote_against=0, 
				total_votes=0,
				percentage_for=0, 
				threshold=r,
				pass_status="fail",
				success = "undetermined")

			p.save()

			next=p.id
			
			# Programming the expiry of the prop.
			
			expiry.apply_async(args=[next], eta=time_object)

			# Updating latest prop time for microconstitution model

			f = MicroCons.objects.get(id=p.microcons_id)
			f.last_prop = datetime.now()
			f.save()	
		
		return render_to_response('prop_confirm.html', {'diff': diffhtml, 'time_object': time_object, 
			'hours_number': hours_number, 'micro_cons': r}, context_instance=RequestContext(request))

	else:
		
		# Put together initial data for the form.
		q = (Articles.objects.filter(cons_id=articleid).order_by('version_id').reverse())[:1]
		data = q[0]
		first = data.articlecontent

		# initial = first.encode("utf8")
		thesis = MicroCons.objects.get(id__contains=articleid).thesis
		
		# Displaying initial data in form.
		
		populate = MicroCons.objects.get(id=articleid)
		form = PropForm(initial={'article': first})

	return render_to_response(
		'edit_article.html', 
		{
		'form': form, 
		'thesis': thesis
		}, 
		context_instance=RequestContext(request)
		)

def view_article_props(request, articleid):
	htmldiff = Props.objects.filter(microcons_id__contains=articleid)
	try:
		prop = Props.objects.get(id=articleid)
	except Props.DoesNotExist:
		prop = None
	return render_to_response(
		'article_props.html', 
		{
		'articleid': articleid, 
		'displaydiff': htmldiff, 
		'prop':prop
		}, 
		context_instance=RequestContext(request)
		)

def view_single_prop(request, propid):
	prop = Props.objects.get(id=propid)
	longdiff = Props.objects.get(id=propid).long_diff
	return render_to_response('single_prop.html', {'prop':prop, 'propid':propid, 'longdiff':longdiff}, context_instance=RequestContext(request))

def time_convert(d):
	now=datetime.utcnow()
	raw_expiry=d
	expiry=raw_expiry.replace(tzinfo=None)
	amount=expiry-now
	return amount

def view_latest_props(request):
	prop = (Props.objects.order_by('createtime').reverse())[:5]
	
	for row in prop:
		d=row.expiry_time
		row.new_field = time_convert(d)

	return render_to_response(
		'latest_props.html', 
		{
		'prop':prop,
		}, 
		context_instance=RequestContext(request)
		)
 
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


# LIST OF Props

# @login_required
# def home(request):

# 	# name of current user
# 	person = request.user
	
# 	# Grab user object
# 	user_set = User.objects.get(username=person)
	
# 	# grab user id from object
# 	user_number = user_set.id

# 	# query set to grab articles/microcons that the user is following
# 	q_set = Follow.objects.filter(user_id=user_number).values_list('target_microcons_id')
	
# 	# formatting data
# 	result = map(list, q_set)
# 	next=sum(result, [])

# 	# building list of props for constitutions that user is following.
# 	elements=[]
# 	for i in next:
# 		results=Props.objects.filter(microcons_id=i)
# 		elements.append(results)

# 	# chain together lists of lists (which are results)
# 	props=list(itertools.chain.from_iterable(elements))

# 	return  render_to_response(
# 		'home.html', 
# 		{
# 		'person': person, 
# 		'props': props,}
# 		, 
# 		context_instance=RequestContext(request)
# 		)
