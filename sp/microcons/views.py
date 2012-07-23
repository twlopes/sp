from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.microcons.models import MicroConsModelForm, MicroCons
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from guardian.shortcuts import assign
from django.contrib.auth.models import User, Permission, Group
from follow import utils

@login_required
def micro_cons(request):
	errors = []
	
	# Bootstrap toolkit specification

	layout = 'horizontal'

	if request.method == 'POST':
		form = MicroConsModelForm(request.POST)
		if form.is_valid():
			business = form.save(commit=False)
			business.director = request.user
			
			business.save()
			form.save()	
			
			next = business.id
			nexto = business.director
			
			constitution = MicroCons.objects.get(id=next)
			user = User.objects.get(username=nexto)

			assign('change_microcons', user, constitution)


			utils.follow(user, constitution)
			
			return HttpResponseRedirect('/done')
	else:
		form = MicroConsModelForm()
	return render_to_response('cons_form.html', {'form': form}, 
		context_instance=RequestContext(request, {'layout': layout,}))

def micro_done(request):
	return render_to_response('Done.html', context_instance=RequestContext(request))