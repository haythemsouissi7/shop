from django.shortcuts import render
from datetime import datetime
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
from produit.models import Boutique, Produit
from produit.forms import BoutiqueForm,  ProduitForm
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
from promotion.models import Promotion
from collection.models import Collection

now=datetime.now()  
class DetailView(generic.DetailView):
    model = Produit
    template_name = 'discover/detail-produit.html'


def Detail0(request,produit_id):
    produit=get_object_or_404(Produit ,pk=produit_id)
    
    likke=Like.objects.filter(produit=produit)
    likers = []
    for like in likke:
        likers.append(like.user)
 
    num=likke.count() 
    return render(request,'discover/detail-produit.html',{'produit':produit,'likks':likke,'user':request.user,'likers':likers,'num':num})
  



def post_list3(request, boutique_id):
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    list_produit = Produit.objects.filter(boutique=boutique)
    paginator = Paginator(list_produit,100)
    page = request.GET.get('page')
    try:
        produits= paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    return render(request, 'discover/detail.html',{'page':page, 'produits1':produits, 'boutique':boutique})


def visite_boutique(request, boutique_id):
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    list_produit = Produit.objects.filter(boutique=boutique)
    paginator = Paginator(list_produit,8)
    page = request.GET.get('page')
    prod_promo=Promotion.objects.filter(is_active=True)
    product=[]
    for k in prod_promo:
        if k.is_active:
            product.append(k.produit)
    try:
        produits= paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    return render(request, 'discover/visite_boutique.html',{ 'produits_boutique':produits, 'boutique':boutique,'now':now,'promo':prod_promo,'products':product,'page':page, 'produitsfilters':produits,'bijoux':list_produit.filter(categorie="bijoux ").count(),'maison':list_produit.filter(categorie="maison et ameublement").count(),'vetements':list_produit.filter(categorie="vetements ").count(), 'art':list_produit.filter(categorie="art et collections").count(),'accessoires':list_produit.filter(categorie="accessoires ").count(),
        'sac': list_produit.filter(categorie="sacs et bagages").count(),'mariage':list_produit.filter(categorie="mariage ").count(),'minslider': min( [post['prix'] for post in list_produit.values('prix')]),
            'maxslider': max([post['prix'] for post in list_produit.values('prix')]),})



def post_list(request):
    list_produit = Produit.objects.filter(etat='active')
    paginator = Paginator(list_produit,8)
    page = request.GET.get('page')
    print("hello")

    prod_promo=Promotion.objects.filter(is_active=True)
    product=[]
    for k in prod_promo:
        if k.is_active:
            product.append(k.produit)

    collections=Collection.objects.filter(is_active=True)
    produit_in_collection=[]
    for collection in collections:
        produits=collection.produit.all()
        for produit in produits:
            produit_in_collection.append(produit)



    print(produit_in_collection)
    try:
        produits= paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    if not request.user.is_authenticated():
        return render(request, 'discover/descaver_sans_login.html',{'now':now,'promo':prod_promo,'page':page, 'bijoux':list_produit.filter(categorie="bijoux ").count(),'maison':list_produit.filter(categorie="maison et ameublement").count(),'vetements':list_produit.filter(categorie="vetements ").count(), 'art':list_produit.filter(categorie="art et collections").count(),'accessoires':list_produit.filter(categorie="accessoires ").count(),
        'sac': list_produit.filter(categorie="sacs et bagages").count(),'mariage':list_produit.filter(categorie="mariage ").count(),'produitsfilters':produits,  'minslider': min( [post['prix'] for post in list_produit.values('prix')]),
            'maxslider': max([post['prix'] for post in list_produit.values('prix')]),'produit_in_collection':produit_in_collection})
    else:  
        return render(request, 'discover/base2.html',{'now':now,'promo':prod_promo,'products':product,'page':page, 'produitsfilters':produits,'bijoux':list_produit.filter(categorie="bijoux ").count(),'maison':list_produit.filter(categorie="maison et ameublement").count(),'vetements':list_produit.filter(categorie="vetements ").count(), 'art':list_produit.filter(categorie="art et collections").count(),'accessoires':list_produit.filter(categorie="accessoires ").count(),
        'sac': list_produit.filter(categorie="sacs et bagages").count(),'mariage':list_produit.filter(categorie="mariage ").count(),'minslider': min( [post['prix'] for post in list_produit.values('prix')]),
            'maxslider': max([post['prix'] for post in list_produit.values('prix')]),'produit_in_collection':produit_in_collection})




def filter2(request):

    catego = request.GET.get("catego")
    b = request.GET.get("b",'10,100')
    valeure=b.split(',')
    min0= int(valeure[0])
    max0= int(valeure[1])

    type = request.GET.get("type")
    recherche = request.GET.get("recherche")

    order = request.GET.get("order")

    flashe= request.GET.get('flashe')
    regular= request.GET.get('regular')

    minpromo=request.GET.get('minpromo')
    maxpromo=request.GET.get('maxprmo')

    prod_promo=Promotion.objects.filter(is_active=True)
    product=[]
    for k in prod_promo:
        if k.is_active:
            product.append(k.produit)

    collections=Collection.objects.filter(is_active=True)
    produit_in_collection=[]
    for collection in collections:
        produits=collection.produit.all()
        for produit in produits:
            produit_in_collection.append(produit)




    
    produit_results = Produit.objects.filter(etat='active')
   
    
    
    
    if recherche:

        produit_results = produit_results.filter(
               Q(title__contains=recherche) | Q(descreption__contains=recherche)).distinct()
    if catego!=None:
        produit_results = produit_results.filter(Q(categorie__contains=catego)
                                                 ).distinct()
    if type!=None:
        if type!="0":


            produit_results = produit_results.filter(
                 Q(type__contains=type)
            ).distinct()


    produit_results = produit_results.filter(
        Q(prix__lte=max0)&Q(prix__gte=min0)
    ).distinct()

    if order!=None:
        if order =="croissanttime":
            produit_results=produit_results.order_by('dat')
        if order =="decroissanttime":
            produit_results=produit_results.order_by('-dat')

        if order == "croissantprix":
            produit_results = produit_results.order_by('prix')
        if order == "decroissantprix":
            produit_results = produit_results.order_by('-prix')

    filters = "order="+str(order)+"&catego="+str(catego)+"&recherche="+str(recherche)+"&type="+str(type)+"&recherche="+str(recherche)

    if flashe:
       
        pro=produit_results.filter(promotion__is_active=True, promotion__promo_type="flash")
       

        produit_results=pro
        print("produit in promotion flashe")
        print(produit_results)
        if minpromo and maxpromo:
            produit_results=produit_results.filter( Q(promotion__discount__gte=minpromo)&Q(promotion__discount__lte=maxpromo)).distinct()
        else:
            if minpromo:
                produit_results=produit_results.filter( Q(promotion__discount__gte=minpromo)).distinct()
            if maxpromo:
                produit_results=produit_results.filter( Q(promotion__discount__lte=minpromo)).distinct()

        
    elif regular:
        pro=produit_results.filter(promotion__is_active=True,promotion__promo_type="regular")
       

        produit_results=pro
        print("produit in promotion")
        print(produit_results)
        if minpromo and maxpromo:
            produit_results=produit_results.filter( Q(promotion__discount__gte=minpromo)&Q(promotion__discount__lte=maxpromo)).distinct()
        else:
            if minpromo:
                produit_results=produit_results.filter( Q(promotion__discount__gte=minpromo)).distinct()
            if maxpromo:
                produit_results=produit_results.filter( Q(promotion__discount__lte=minpromo)).distinct()


    list_produit = produit_results
    paginator = Paginator(list_produit, 8)
    page = request.GET.get('page')
    try:
        produit_resultss = paginator.page(page)
    except PageNotAnInteger:
        produit_resultss = paginator.page(1)
    except EmptyPage:
        produit_resultss = paginator.page(paginator.num_pages)
   
    
  
    
    context={'page':page,'filters':filters,'promo':prod_promo,'products':product,
        'minslider':min([post['prix'] for post in Produit.objects.all().values('prix')]),
        'maxslider': max([post['prix'] for post in Produit.objects.all().values('prix')]),
        'produitsfilters': produit_resultss,'bijoux':produit_results.filter(categorie="bijoux ").count(),'maison':produit_results.filter(categorie="maison et ameublement").count(),'vetements':produit_results.filter(categorie="vetements ").count(), 'art':produit_results.filter(categorie="art et collections").count(),'accessoires':produit_results.filter(categorie="accessoires ").count(),
        'sac': produit_results.filter(categorie="sacs et bagages").count(),'mariage':produit_results.filter(categorie="mariage ").count(),'valeur':min0,}

    print(context['minslider'])
    return render(request, 'discover/base2.html', context,)


