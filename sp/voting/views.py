from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from sp.props.models import Props
from sp.props.forms import PropForm
from sp.microcons.models import MicroCons
from sp.voting.models import Vote_Records
from sp.props.diff_match_patch import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from guardian.decorators import permission_required_or_403
from django.contrib.auth.models import User, Permission, Group
from guardian.shortcuts import assign


def status(percentage_up, threshold):
	if percentage_up >= threshold:
		return "pass"
	else:
		return "fail"

@login_required
def up_vote(request, propid):

	u = request.user
	u_id=User.objects.get(username=u).id


	qset = Props.objects.get(id=propid)
	g = qset.currency
	f = qset.microcons_id
	c = MicroCons.objects.get(id=f)

	j = u.has_perm('change_microcons', c)

	if j is True:

		if g == "current":

			# Pull out information to update.

			upvote = qset.vote_for
			downvote = qset.vote_against
			threshold = qset.threshold

			# Update information for saving to database

			new_up_vote = upvote + 1
			total_votes = 	new_up_vote + downvote
			percentage_up = float(new_up_vote) / float(total_votes) * 100

			pass_or_fail = status(percentage_up, threshold)

			# Save into object instance.

			qset.vote_for = new_up_vote
			qset.percentage_for = percentage_up
			qset.pass_status = pass_or_fail


			# Send back into database.

			qset.save()

			# Save vote records

			record = Vote_Records(user_id=u_id, target_prop=propid, for_against="for")
			record.save()


			return render_to_response('thanks_for_vote.html', context_instance=RequestContext(request))

		else:

			return render_to_response('prop_expired.html', context_instance=RequestContext(request))

	else:
		
		return render_to_response('no_permission.html', context_instance=RequestContext(request))

@login_required
def down_vote(request, propid):

	u = request.user
	u_id=User.objects.get(username=u).id


	qset = Props.objects.get(id=propid)
	g = qset.currency
	f = qset.microcons_id
	c = MicroCons.objects.get(id=f)

	j = u.has_perm('change_microcons', c)

	if j is True:

		if g == "current":

			# Pull out information to update.

			upvote = qset.vote_for
			downvote = qset.vote_against
			threshold = qset.threshold

			# Update information for saving to database

			new_down_vote = downvote + 1
			total_votes = 	new_down_vote + upvote
			percentage_up = float(upvote) / float(total_votes) * 100

			pass_or_fail = status(percentage_up, threshold)

			# Save into object instance.

			qset.vote_against = new_down_vote
			qset.percentage_for = percentage_up
			qset.pass_status = pass_or_fail


			# Send back into database.

			qset.save()

			# Save vote records

			record = Vote_Records(user_id=u_id, target_prop=propid, for_against="against")
			record.save()


			return render_to_response('thanks_for_vote.html', context_instance=RequestContext(request))

		else:

			return render_to_response('prop_expired.html', context_instance=RequestContext(request))

	else:
		
		return render_to_response('no_permission.html', context_instance=RequestContext(request))