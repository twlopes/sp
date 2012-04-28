from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# from sp.microcons.forms import MicroConsForm
from sp.microcons.models import MicroConsModelForm

def micro_cons(request):
	errors = []
	if request.method == 'POST':
		form = MicroConsModelForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/done/')
	else:
		form = MicroConsModelForm()
	return render_to_response('cons_form.html', {'form': form})

def micro_done(request):
	return render_to_response('done.html')