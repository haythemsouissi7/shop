from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.shortcuts import render
import pytz
# Create your views here.
from django.shortcuts import render
import json
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from produit.models import Produit,Like,Love
from projet5.decorators import ajax_required
import dateutil.parser
# Create your views here.
from django.views import generic
from messenger.forms import AttacheForm
from .models import Promotion
from .forms import PromotionForm,promotionstartform
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
from produit.models import Boutique
from collection.models import Collection

from celery import Task
from datetime import datetime, timedelta
from .tasks import activate,desactivate
now = timezone.now()

def formpromotion(request):
	boutique=Boutique.objects.get(user=request.user)
	collection=Collection.objects.filter(owner=request.user)
	return render(request, 'promotion/create_promotion.html',{'boutique':boutique,'collections':collection})

def formpromotion_failed(request):
	boutique=Boutique.objects.get(user=request.user)
	collection=Collection.objects.filter(owner=request.user)
	return render(request, 'promotion/create_promotion_failed.html',{'boutique':boutique,'collections':collection})

def formpromotion_failed_collection(request):
	boutique=Boutique.objects.get(user=request.user)
	collection=Collection.objects.filter(owner=request.user)
	return render(request, 'promotion/create_promotion_failed_collection.html',{'boutique':boutique,'collections':collection})


def create_promotion0(request):
    form = PromotionForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
      
        
        promotion = form.save(commit=False)
        
      
        promotion.save()
        return redirect('/discover/produits/')
    context = {
        
        'form': form,
    }
    return render(request, 'promotion/create_promotion.html', context)

def get_collection(request):
	if request.method =='POST':
		col=request.POST.get('collection')
		print(col)

		return render(request,'promotion/list_collection.html')


def create_promotion(request):
	time_zone=request.POST.get('time_zone')
	discount = request.POST.get('discount')
	start_end=request.POST.get('bdaytime')
	start=request.POST.get('start')
	end= request.POST.get('end')
	start_flash=request.POST.get('start_flash')
	end_flash=request.POST.get('end_flash')
	type_promo=request.POST.get('promo')
	type_collection=request.POST.get('collect')

	boutique=Boutique.objects.get(user=request.user)
	produits1=boutique.produit_set.all()	
	produt_promotion=[]
	for produit in produits1:
		promos = Promotion.objects.filter(produit=produit)	
		for x in promos:
			produt_promotion.append(x.produit)

	
	collections1=Collection.objects.filter(owner=request.user)
	
	collection_promotion=[]
	for col in collections1:
		promos1 = Promotion.objects.filter(collection=col)	
		for x in promos1:
			collection_promotion.append(x.collection)

	if type_collection=="c":
		obj_id=request.POST.get('collection_chose')
		obj=Collection.objects.get(pk=obj_id)
		if obj in collection_promotion:
			return redirect('/promotion/form_failed_collection/')
		else:
			promotion=Promotion(discount=discount)
			promotion.collection=obj
			promotion.types="c"
	elif type_collection=="p":
		prod_id=request.POST.get('produit_chose')
		prod=Produit.objects.get(pk=prod_id)
		if prod in produt_promotion:
			tests=Promotion.objects.filter(produit=prod)
			if start_end:
				start1=str(start_end).split('-')
				end1=str(start_end).split('-')
			if start:
				start1=str(start).split('-')
				st=datetime(int(start1[0]),int(start1[1]),int(start1[2]))
		
			if end:
				end1=str(end).split('-')
				en=datetime(int(end1[0]),int(end1[1]),int(end1[2]))
			if start_flash:
				stime1=str(start_flash).split(':')
				etime1=str(end_flash).split(':')
				en=datetime(int(end1[0]),int(end1[1]),int(end1[2]),int(etime1[0]),int(etime1[1]))
				st=datetime(int(start1[0]),int(start1[1]),int(start1[2]),int(stime1[0]),int(stime1[1]))
			en = pytz.utc.localize(en)
			st = pytz.utc.localize(st)
			for test in tests:
				if test.start < now and test.end>now:
					return redirect('/promotion/form_failed/')
				if test.start>en:
					promotion=Promotion(discount=discount)
					promotion.produit=prod
					promotion.types="p"
				if test.end <st:
					promotion=Promotion(discount=discount)
					promotion.produit=prod
					promotion.types="p"
				else:
					return redirect('/promotion/form_failed/')

		else:
			promotion=Promotion(discount=discount)
			promotion.produit=prod
			promotion.types="p"


	if type_promo=="flash":
		promotion.promo_type="flash"
		start=start_end
		start=str(start).split('-')
		stime=str(start_flash).split(':')
		etime=str(end_flash).split(':')
		promotion.start=datetime(int(start[0]),int(start[1]),int(start[2]),int(stime[0])+int(int(time_zone)/60),int(stime[1])+int(int(time_zone)%60))
		promotion.end=datetime(int(start[0]),int(start[1]),int(start[2]),int(etime[0])+int(int(time_zone)/60),int(etime[1])+int(int(time_zone)%60))
		print(promotion.start)
		print(promotion.end)
		promotion.save()
		print("start"+str(promotion.start))
		print("end"+str(promotion.end))
		activate.apply_async([promotion.id], eta=promotion.start)
		promotion.start=datetime(int(start[0]),int(start[1]),int(start[2]),int(stime[0])+int(int(time_zone)/60),int(stime[1])+int(int(time_zone)%60))
		promotion.end=datetime(int(start[0]),int(start[1]),int(start[2]),int(etime[0])+int(int(time_zone)/60),int(etime[1])+int(int(time_zone)%60))
	
		desactivate.apply_async([promotion.id], eta=promotion.end)
	elif type_promo=="regular":	
		promotion.promo_type="regular"

		start=str(start).split('-')
		end=str(end).split('-')
		
		promotion.start=datetime(int(start[0]),int(start[1]),int(start[2]))
		promotion.end=datetime(int(end[0]),int(end[1]),int(end[2]))
		promotion.save()
		activate.apply_async([promotion.id], eta=promotion.start)
		promotion.start=datetime(int(start[0]),int(start[1]),int(start[2]))
		promotion.end=datetime(int(end[0]),int(end[1]),int(end[2]))
		desactivate.apply_async([promotion.id], eta=promotion.end)
	
	promotion.save()
	user=request.user
	boutique=Boutique.objects.get(user=user)
	user=boutique.user
	produits=boutique.produit_set.all()
	collections=Collection.objects.filter(owner=user)
	promo=[]
	for produit in produits:
		promos = Promotion.objects.filter(produit=produit)	
		for x in promos:
			promo.append(x)
	for collection in collections:
		collect=Promotion.objects.filter(collection=collection)
		for y in collect:
			promo.append(y)
	

	return render(request,'promotion/promotions.html',{'promotions':promo,'promotion':promotion,'boutique':boutique})
	

def promotions(request,boutique_id):
	boutique=Boutique.objects.get(pk=boutique_id)
	user=boutique.user
	produits=boutique.produit_set.all()
	collections=Collection.objects.filter(owner=user)
	promo=[]
	for produit in produits:
		promos = Promotion.objects.filter(produit=produit)	
		for x in promos:
			promo.append(x)
	for collection in collections:
		collect=Promotion.objects.filter(collection=collection)
		for y in collect:
			promo.append(y)

	return render(request,'promotion/promotions.html',{'promotions':promo,'boutique':boutique})


def get_Datas(request,promotion_id):

    time= Promotion.objects.get(pk=promotion_id)
    data['cc']=time.get_time()
   
    return HttpResponse(json.dumps(data), content_type='application/json')



