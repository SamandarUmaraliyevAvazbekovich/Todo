from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

def home(request):
	a = Maqola.objects.all()
	if request.method == 'GET':
		top = request.GET.get('q','')
		
	return render(request,'home.html',{'a':a,'top':top})



def qosh(request):
	if request.method == 'POST':
		form = Maqolaqosh(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else : 
		form = Maqolaqosh()
	return render(request,'qosh.html',{'form':form})


def oqi(request,oqi_id):
	a = get_object_or_404(Maqola,id=oqi_id)
	return render(request,'oqi.html',{'a':a})

def edit(request,edit_id):
	edit = Maqola.objects.get(pk=edit_id)
	if request.method == 'POST':
		edit.title = request.POST.get('title')
		edit.context = request.POST.get('context')
		edit.save()
		return redirect('home')
	return render(request,'edit.html',{'edit':edit})

def delete(request,del_id):
	b = Maqola.objects.get(id=del_id)
	b.delete()
	return redirect('home')


