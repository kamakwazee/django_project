from django.shortcuts import render

from .forms import SomeTextForm

def index(request):
	if request.method == 'POST':
		form = SomeTextForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = SomeTextForm()
	return render(request, 'textapp/index.html', {'form':form})
