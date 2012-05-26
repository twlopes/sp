from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from sp.props.models import Props
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.props.diff_match_patch import *
from django.contrib.auth.decorators import login_required

def up_vote(request, propid):
	
	count = Vote.objects.filter(prop_id__contains=propid).values()
	
	p = Vote(prop_id=propid, vote_for=count )
	return render_to_response('thanks_for_vote.html', {'ello': ello}

# def down_vote(request, propid):
# 	# function
# 	return render_to_response('thanks_for_vote.html', {'ello': ello}
# 	
# def view_vote_status(request, propid):
# 	# function
# 	return render_to_response('thanks_for_vote.html', {'ello': ello}
# 	
# p = Props(idversions=articleid, maindiff=diff, patch=patchdata, htmldiff=diffhtml)
# 				p.save()



				
