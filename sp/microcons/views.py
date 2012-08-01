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
		# cons_form = MicroConsModelForm(request.POST, prefix = "cons_form")
		article_form = ArticleModelForm(request.POST)
		# article_form = ArticleModelForm(request.POST, prefix = "article_form")
		
		if cons_form.is_valid() and article_form.is_valid():
			print "all validation passed"
			# cons = cons_form.save(commit=False)
			# cons.director = request.user
			
			cons_form.save()
			article_form.save()

			# next = cons.id
			# nexto = cons.director
			
			# constitution = MicroCons.objects.get(id=next)
			# user = User.objects.get(username=nexto)

			# assign('change_microcons', user, constitution)


			# utils.follow(user, constitution)
			
			return HttpResponseRedirect('/done')
	else:
		cons_form = MicroConsModelForm()
		article_form = ArticleModelForm()
	return render_to_response('cons_form.html', {'form': cons_form, 'article_form': article_form}, 
		context_instance=RequestContext(request, {'layout': layout,}))

def micro_done(request):
	return render_to_response('Done.html', context_instance=RequestContext(request))