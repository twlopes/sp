from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from sp.microcons.models import MicroConsModelForm, MicroCons
from sp.article.models import ArticleModelForm
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
		
		cons_form = MicroConsModelForm(request.POST)
		article_form = ArticleModelForm(request.POST)
		
		if cons_form.is_valid() and article_form.is_valid():
			
			cons = cons_form.save(commit=False)
			article = article_form.save(commit=False)
			cons.director = request.user
			
			# saving constitution model form

			cons_form.save()
			
			# Grab id and director name for cons just created

			saved_cons_id = cons.id
			saved_cons_director = cons.director
			
			# Save constitution id to the article model form.

			article.cons_id = saved_cons_id
			article.version_id = 1
			article_form.save()

			# Grab relevant objects

			constitution = MicroCons.objects.get(id=saved_cons_id)
			user = User.objects.get(username=saved_cons_director)

			# Give user permission for constitution

			assign('change_microcons', user, constitution)

			# Make user follow changes to constitution

			utils.follow(user, constitution)
			
			return HttpResponseRedirect('/done')
	else:
		cons_form = MicroConsModelForm()
		article_form = ArticleModelForm()
	return render_to_response('cons_form.html', {'form': cons_form, 'article_form': article_form}, 
		context_instance=RequestContext(request, {'layout': layout,}))

def micro_done(request):
	return render_to_response('Done.html', context_instance=RequestContext(request))