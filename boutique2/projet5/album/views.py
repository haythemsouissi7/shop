from django.shortcuts import render

# Create your views here.
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
# Create your views here.
from django.views import generic
from messenger.forms import AttacheForm
from .models import Album,Picture
from .forms import AlbumForm,PictureForm
from django.contrib.auth import authenticate, login
from produit.models import Boutique
from django.http import JsonResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from authentication.models import Utilisateur
import json





AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_album(request,boutique_id):
	boutique = Boutique.objects.get(pk=boutique_id)
	user = boutique.user
	title = request.POST.get('title')
	album=Album(user=user,name=title)
	album.image= request.POST.get('image')
	form = AlbumForm(request.POST, request.FILES, instance=album)
	
	if form.is_valid():
		obj = form.save(commit=False)
		
		obj.save()
	
	list_album=Album.objects.filter(user=boutique.user)
	return render(request,'album/albums.html',{'albums':list_album,'boutique':boutique})
	

def formulaire(request,boutique_id):
	boutique = Boutique.objects.get(pk=boutique_id)
	return render(request,'album/create_album.html',{'boutique':boutique})


def albums(request,boutique_id):
	boutique = Boutique.objects.get(pk=boutique_id)
	list_album=Album.objects.filter(user=boutique.user)
	return render(request,'album/albums.html',{'albums':list_album,'boutique':boutique})




def show_picture(request,album_id):
	album= Album.objects.get(pk= album_id)
	pic=Picture.objects.filter(album=album)
	return render(request,'album/picturs.html',{'album':album,'picturs':pic})



def add_picture(request,album_id):
	album= Album.objects.get(pk= album_id)

	image=Picture(album=album)
	picture = request.FILES.get('picture')
	print(type(image))
	image.logo = picture
	image.save()
	'''
	if form.is_valid():
		print("valid")
		obj = form.save(commit=False)
		
		obj.save()
	else:
		print("invalid")
	'''
	album2= Album.objects.get(pk= album_id)
	pic=Picture.objects.filter(album=album)

	print("success ..")
	return render(request,'album/picturs.html',{'album':album2,'picturs':pic})
	














