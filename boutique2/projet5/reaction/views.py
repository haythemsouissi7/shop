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
from produit.models import Boutique, Produit

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

from .models import Reaction
from notification.models import Notification



@login_required
@ajax_required
def react(request, pk):

    data = {}
    product = Produit.objects.get(pk=pk)
    reaction = request.GET.get('reaction')
    has_reacted = Reaction.objects.filter(user=request.user, product=product).count() == 1
    reaction_choices = Reaction.get_choices()
    obj=product.reaction_set.filter(type="smile").count()
    if has_reacted:
        reaction_obj = request.user.reaction_set.get(product=product)
        if reaction in reaction_choices:

            if reaction_obj.type != reaction:
                reaction_obj.type = reaction
                Notification.send(from_user=request.user, to_user=product.boutique.user, product=product, type=reaction)
                reaction_obj.save()
        		
            else:
                reaction_obj.delete()
            data['reaction'] = reaction

        elif not reaction:
            reaction_obj.delete()
            data['reaction'] = ''

    elif reaction in  reaction_choices:
        Reaction.objects.create(user=request.user, product=product, type=reaction)
        Notification.send(from_user=request.user, to_user=product.boutique.user, product=product, type=reaction)

        data['reaction'] = reaction;

    data['count'] = product.reaction_set.count()
    #data['count_smile']= obj
    normal= Reaction.objects.filter(product= product, type='normal').count()
    smile= Reaction.objects.filter(product= product, type='smile').count()
    love= Reaction.objects.filter(product= product, type='love').count() 
    wish= Reaction.objects.filter(product= product, type='wish').count()
    data['normal'] = normal
    data['smile'] = smile
    data['love'] = love
    data['wish'] = wish
    print(obj)
    
    return HttpResponse(json.dumps(data), content_type='application/json')




def Nreaction(request, produit_id):
    produit= Produit.objects.get(pk=produit_id)
    normal= Reaction.objects.filter(product= produit, type='normal').count()
    smile= Reaction.objects.filter(product= produit, type='smile').count()
    love= Reaction.objects.filter(product= produit, type='love').count() 
    wish= Reaction.objects.filter(product= produit, type='wish').count()
    normal_list = Reaction.objects.filter(product=produit, type='normal')
    list_normal=[]
    for reacter in normal_list:
        list_normal.append(reacter.user)

    smile_list = Reaction.objects.filter(product=produit, type='smile')
    list_smile=[]
    for reacter in smile_list:
        list_smile.append(reacter.user)
    love_list = Reaction.objects.filter(product=produit, type='love')
    list_love=[]
    for reacter in love_list:
        list_love.append(reacter.user)
    wish_list = Reaction.objects.filter(product=produit, type='wish')
    list_wish=[]
    for reacter in wish_list:
        list_wish.append(reacter.user)

    return render(request,'produit/pagelikes.html',{'normal':normal,'smile':smile,'love':love,'wish':wish,'list_normal':list_normal,'list_smile':list_smile,'list_love':list_love,'list_wish':list_wish, 'produit_name':produit.title})



