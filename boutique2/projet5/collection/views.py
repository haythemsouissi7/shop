from django.shortcuts import render
from django.contrib.auth import authenticate, login
from produit.models import Boutique,Produit
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from produit.models import Produit,Like,Love
from projet5.decorators import ajax_required
from messenger.models import Message
from django.views import generic
from messenger.forms import AttacheForm


from django.contrib.auth import authenticate, login

from django.http import JsonResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from authentication.models import Utilisateur
import json
from .forms import CollectionForm
from collection.models import Collection

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def collection(request):
	boutique=Boutique.objects.get(user=request.user)
	collections=Collection.objects.filter(owner=request.user)
	return render(request,'collection/collections.html',{'boutique':boutique,'collections':collections})

def formulaire_collection(request):
	boutique=Boutique.objects.get(user=request.user)
	collections=Collection.objects.filter(owner=request.user)
	return render(request,'collection/create_collection.html',{'boutique':boutique,'collections':collections})

def create_collection(request):
	title = request.POST.get('title')
	discription = request.POST.get('discription')
	user = request.user
	boutique= Boutique.objects.get(user=user)
	collection = Collection(title=title, discription=discription,owner=user)
	form = CollectionForm(request.POST, request.FILES, instance=collection)
	
	if form.is_valid():
		obj = form.save(commit=False)
		obj.title=title
		obj.discription=discription
		obj.owner=user
		obj.save()
		collection = obj
	if request.POST.getlist("produit", None):
		checked =request.POST.getlist('produit',None)
		for k in checked:
			produits=Produit.objects.get(pk= int(k))
			collection.produit.add(produits)
			collection.save()
	collections=Collection.objects.filter(owner=user)
	return render(request,'collection/collections.html',{'collection':collection,'boutique':boutique,'collections':collections})
	


def detail_collection(request, collection_id):
	collection = Collection.objects.get(pk =collection_id)
	produits= collection.produit.all()
	return render(request,'collection/detail_collection.html',{'produits':produits})




def edit_collection(request,collection_id):
	collection =Collection.objects.get(pk=collection_id)
	produits= collection.produit.all()
	boutique=Boutique.objects.get(user=request.user)
	return render(request,'collection/edit_collection.html',{'collection':collection,'produits':produits,'boutique':boutique})

def edit(request,collection_id):
	collection =Collection.objects.get(pk=collection_id)
	title = request.POST.get('title')
	discription = request.POST.get('discription')
	user = request.user
	boutique= Boutique.objects.get(user=user)


	form = CollectionForm(request.POST, request.FILES, instance=collection)
	
	if form.is_valid():
		obj = form.save(commit=False)
		obj.title=title
		obj.discription=discription
		obj.owner=user
		obj.save()
		collection = obj

	deleted= collection.produit.all()
	for a in deleted:
		collection.produit.remove(a)
	collection.save()
	if request.POST.getlist("produit", None):
		checked =request.POST.getlist('produit',None)
		for k in checked:
			produits=Produit.objects.get(pk= int(k))
			collection.produit.add(produits)
			collection.save()
	collections=Collection.objects.filter(owner=user)
	return render(request,'collection/collections.html',{'collection':collection,'boutique':boutique,'collections':collections})
	
 



def edit_image(request,collection_id):
	collection= Collection.objects.get(pk = collection_id)
	collection.picture = request.FILES['picture']
	collection.save()
	title=request.POST.get('title')
	discription=request.POST.get('discription')
	picture=request.POST.get('picture')
	return redirect('/col/')

def active(request,collection_id):
	collection= Collection.objects.get(pk= collection_id)
	
	try:
		if collection.is_active:
			collection.is_active = False
		else:
			collection.is_active = True
		collection.save()
	except (KeyError, Collection.DoesNotExist):
		return JsonResponse({'success': False})
	else:
		return redirect('/col/')
	





          