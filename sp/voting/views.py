from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from sp.props.models import Props
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.voting.models import Vote
from sp.props.diff_match_patch import *
from django.contrib.auth.decorators import login_required

def up_vote(request, propid):
	
	count = Vote.objects.filter(prop_id__contains=propid).values()
	data = count[0]
	upvote = data['vote_for']
	new_upvote = upvote + 1
	record = Vote.objects.get(prop_id=propid)
	record.vote_for = new_upvote
	record.save()
	return render_to_response('thanks_for_vote.html')

def down_vote(request, propid):

	count = Vote.objects.filter(prop_id__contains=propid).values()
	data = count[0]
	downvote = data['vote_against']
	new_downvote = downvote + 1
	record = Vote.objects.get(prop_id=propid)
	record.vote_against = new_downvote
	record.save()
	return render_to_response('thanks_for_vote.html')



# def down_vote(request, propid):


# 	return render_to_response('thanks_for_vote.html', {'ello': ello}
# 	
# def view_vote_status(request, propid):
# 	# function
# 	return render_to_response('thanks_for_vote.html', {'ello': ello}
# 	
# p = Props(idversions=articleid, maindiff=diff, patch=patchdata, htmldiff=diffhtml)
# 				p.save()



				
