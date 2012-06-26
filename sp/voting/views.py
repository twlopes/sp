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
from django.contrib.auth.decorators import permission_required
from guardian.decorators import permission_required_or_403
from django.contrib.auth.models import User, Permission, Group
from guardian.shortcuts import assign


def status(percentage_up, threshold):
	if percentage_up >= threshold:
		return "Currently Passing"
	else:
		return "Currently Failing"

@login_required
def up_vote(request, propid):
	
# Get the variables together to check permission.	
	
	u = request.user
	m = Props.objects.filter(id=propid).values()
	o = m[0]
	f = o['microcons_id']
	g = o['current_status']

	# Insert code to grab currency status.
	
	c = MicroCons.objects.get(id=f)
	j = u.has_perm('change_microcons', c)

	if j is True:
		
		if g == "current":

			count = Vote.objects.filter(prop_id=propid).values()
			data = count[0]

			# Pull out information to update.

			upvote = data['vote_for']
			downvote = data['vote_against']
			threshold = data['threshold']

			# Update information for saving to database

			new_upvote = upvote + 1
			total_votes = 	new_upvote + downvote
			percentage_up = float(new_upvote) / float(total_votes) * 100

			blah = status(percentage_up, threshold)

			# Pull out instance to update.

			record = Vote.objects.get(prop_id=propid)

			# Save into object instance.

			record.vote_for = new_upvote
			record.percentage_for = percentage_up
			record.current_status = blah

			# Send back into database.

			record.save()

			return render_to_response('thanks_for_vote.html')

		else:

			return render_to_response('prop_expired.html')
		
	else:
		
		return render_to_response('no_permission.html')

@login_required
def down_vote(request, propid):

	u = request.user
	m = Props.objects.filter(id=propid).values()
	o = m[0]
	f = o['microcons_id']
	
	c = MicroCons.objects.get(id=f)
	j = u.has_perm('change_microcons', c)

	if j is True:

		if g == "current":

			count = Vote.objects.filter(prop_id=propid).values()
			data = count[0]

			# Pull out information to update.

			upvote = data['vote_for']
			downvote = data['vote_against']
			threshold = data['threshold']

			# Update information for saving to database

			new_down_vote = downvote + 1
			total_votes = 	new_down_vote + upvote
			percentage_up = float(upvote) / float(total_votes) * 100

			blah = status(percentage_up, threshold)

			# Pull out instance to update.

			record = Vote.objects.get(prop_id=propid)

			# Save into object instance.

			record.vote_against = new_down_vote
			record.percentage_for = percentage_up
			record.current_status = blah

			# Send back into database.

			record.save()

			return render_to_response('thanks_for_vote.html')

		else:

			return render_to_response('prop_expired.html')

	else:
		
		return render_to_response('no_permission.html')