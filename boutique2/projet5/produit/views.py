from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from produit.models import Produit
from projet5.decorators import ajax_required
from messenger.models import Message
# Create your views here.
from django.views import generic
from messenger.forms import AttacheForm
from .models import Boutique, Produit
from .forms import BoutiqueForm,  ProduitForm
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





AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def group_based_upload_to(instance, filename):
    return "image/boutique/{}/{}".format(instance.boutique.name, filename)

def detail(request, boutique_id):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        user = request.user
        boutique = get_object_or_404(Boutique, pk=boutique_id)
        produits1=boutique.produit_set.all()
        return render(request, 'discover/detail.html', {'boutique': boutique, 'user': user,'produits1':produits1})



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        boutiques = Boutique.objects.filter(user=request.user)
        produit_results = Produit.objects.all()
        query = request.GET.get("q")
        if query:
            boutiques = boutiques.filter(
                Q(name__icontains=query)

            ).distinct()
            produit_results = produit_results.filter(
                Q(title__icontains=query)
            ).distinct()
            return render(request, 'produit/index.html', {
                'boutiques': boutiques,
                'produits': produit_results,
            })
        else:
            return render(request, 'produit/index.html', {'boutiques': boutiques})


def recherche(request):

    produit_results = Produit.objects.filter(etat='active')
    query = request.GET.get("q")


    produit_results = produit_results.filter(
           Q(title__contains=query) | Q(descreption__contains=query)).distinct()

    context={
        'bijoux':produit_results.filter(categorie='bijoux').count(),'maison':produit_results.filter(categorie__contains='maison').count(),'sacs':produit_results.filter(categorie__contains='sacs et bagages').count(),'produitsfilters': produit_results,'vetements':produit_results.filter(categorie__contains='vetements').count(),'art':produit_results.filter(categorie__contains='art et collections').count(),
        'accessoires': produit_results.filter(categorie__contains='accessoires').count(),
        'mariage': produit_results.filter(categorie__contains='mariage').count(), }
    return render(request, 'discover/produit-filter.html', context)



def create_boutique(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        if not Utilisateur.objects.filter(user=request.user).exists():
            return render(request, 'authentication/utilisateur.html')

        form = BoutiqueForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            boutique = form.save(commit=False)
            boutique.user = request.user
            boutique.logo = request.FILES['logo']
            file_type = boutique.logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'boutique': boutique,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'produit/create_boutique.html', context)
            boutique.save()
            return render(request, 'discover/detail.html', {'boutique': boutique})
        context = {
            "form": form,
        }
        return render(request, 'produit/create_boutique.html', context)


def create_utilisateur(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        form = BusinessUserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            utilisateur = form.save(commit=False)
            utilisateur.user = request.user
            utilisateur.Picture = request.FILES['Picture']
            file_type = utilisateur.Picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'utilisateur': utilisateur,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'produit/utilisateur.html', context)
                utilisateur.save()
            return render(request, 'discover/detail.html', {'boutique':utilisateur})
        context = {
            "form": form,
        }
        return render(request, 'produit/utilisateur.html', context)

def Activer(request, produit_id):
    album = get_object_or_404(Produit, pk=produit_id)
    try:
        if album.etat == 'active':
            album.etat = 'desactive'
        else:
            album.etat = 'active'
        album.save()
    except (KeyError, Produit.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def DesActiver(request, produit_id):
    try:
        produit = Produit.objects.get(pk=produit_id)
        print(produit.boutique.user)
        print(request.user)
        if produit.boutique.user == request.user:
           if produit.etat == "desavctive" :
               produit.etat = "active"
           else:
             produit.etat = "desactive"
           produit.save()

           return JsonResponse({'success':True})

        else:

         return JsonResponse({'erreur':'Vous n''avez pas le droit de modifier ce produit. '})

    except Produit.DoesNotExist:
     return JsonResponse({'error' : 'object dose not exist'})


def delete_boutique(request, boutique_id):
    boutique = Boutique.objects.get(pk=boutique_id)
    boutique.delete()
    boutiques = Boutique.objects.filter(user=request.user)
    return render(request, 'produit/index.html', {'boutique': boutiques})





def create_produit(request, boutique_id):
    form = ProduitForm(request.POST or None, request.FILES or None)
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    if form.is_valid():
        boutiques_produits = boutique.produit_set.all()
        for s in boutiques_produits:
            if s.title == form.cleaned_data.get("title"):
                context = {
                    'boutique': boutique,
                    'form': form,
                    'error_message': 'You already added that produit',
                }
                return render(request, 'produit/create_produit.html', context)
        produit = form.save(commit=False)
        produit.boutique = boutique
        produit.user = request.user
        produit.save()
        return redirect('/discover/aa/'+str(boutique.id))
    context = {
        'boutique': boutique,
        'form': form,
    }
    return render(request, 'produit/create_produit.html', context)


def duppliquer_produit(request, produit_id):

    produit = Produit.objects.get( pk=produit_id)
    produit.id = None
    produit.save()

    return redirect('/discover/aa/'+str(produit.boutique.id))



def post_update(request, produit_id):
    instance = get_object_or_404(Produit, id=produit_id)
    form = ProduitForm(request.POST or None,request.FILES or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.image1= request.POST.get('image1')or instance.image1
        instance.image2= request.POST.get('image2')or instance.image2
        instance.image3= request.POST.get('image3')or instance.image3     
        instance.save()

        return HttpResponseRedirect('/discover/aa/'+str(instance.boutique.id))
    context = {'form': form,}
    return render(request,'produit/create_produit.html',context)

def delete_produit(request, boutique_id, produit_id):
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    produit = Produit.objects.get(pk=produit_id)
    produit.delete()
    return redirect('/discover/aa/'+str(boutique.id))











# def afficher(request):

#     produit_results = Produit.objects.all()
#     query1 = request.GET.get("min1")
#     query2 = request.GET.get("max1")
#     categ = request.GET.get("categ")
#     type = request.GET.get("type")
#     rech = request.GET.get("q")



#     if query1 and query2 and categ and type:
#         if type=="0":

#             produit_results = produit_results.filter(
#                 Q(prix__range={query1, query2})&Q(categorie=categ)
#             ).distinct()

#         else:
#             produit_results = produit_results.filter(
#                 Q(prix__range={query1, query2}) & Q(categorie=categ) & Q(type=type)
#             ).distinct()
#     elif query1 and query2 and categ:
#         produit_results = produit_results.filter(
#             Q(prix__range={query1, query2}) & Q(categorie=categ)
#         ).distinct()
#     elif categ and type == "0":
#         produit_results = produit_results.filter(
#            Q(categorie=categ)
#         ).distinct()
#     elif categ and type != "0":
#         produit_results = produit_results.filter(
#             Q(categorie=categ) & Q(type=type)
#         ).distinct()
#     elif type and query1 and query2:
#         produit_results = produit_results.filter(
#             Q(prix__range={query1, query2})& Q(type=type)
#         ).distinct()
#     elif categ:
#         produit_results = produit_results.filter(categorie=categ)
#     elif type:
#         produit_results = produit_results.filter(type=type)

#     elif query1 and query2:
#         produit_results = produit_results.filter(
#             Q(prix__range={query1, query2})
#         ).distinct()
#     else:produit_results = Produit.objects.all()
#     return render(request,'produit/produit-filter.html', {'produitsfilters': produit_results,'count':produit_results.count(),'categorie':categ} )











def searchproduit(request):
    user=request.user
    produit_results = Produit.objects.filter(boutique__user_id=user.id)
    query = request.GET.get("q")


    produit_results = produit_results.filter(
           Q(title__contains=query) ).distinct()

    context={

        'produitsfilters':produit_results,}
    return render(request, 'produit/send_image.html', context)

  
    
@ajax_required
def users(request):
    users = Produit.objects.filter(etat='active')
    dump = []
    template = '{0} ({1})'
    for user in users[1:4]:
       
      
        dump.append(user.title)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')





def attache_image(request):
    if request.method == 'POST':
        
        from_user = request.user
        to_user_username = request.POST.get('to')
        
        to_user = User.objects.get(username=to_user_username)
        form = AttacheForm(request.POST or None,request.FILES or None)
        
        attache = form.save(commit=False)
        msg = Message.send_message(from_user=from_user, to_user=to_user, message=None,objet=None, produit=None)
        attache.message = msg
        
        attache.save()
        
       

        
    to_user_username = request.POST.get('to')
    url=request.POST.get('url')
    id_boutique=request.GET.get('boutic')
    return render(request, 'messenger/includes/partial_message.html',
                        {'message': msg})



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
                reaction_obj.save()
        
            else:
                reaction_obj.delete()
            data['reaction'] = reaction

        elif not reaction:
            reaction_obj.delete()
            data['reaction'] = ''

    elif reaction in  reaction_choices:
        Reaction.objects.create(user=request.user, product=product, type=reaction)


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



