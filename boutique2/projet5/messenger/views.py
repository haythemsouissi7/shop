import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from produit.models import Produit
from authentication.models import Utilisateur
from projet5.decorators import ajax_required
from messenger.models import Message,Attache
from messenger.forms import AttacheForm
from django.db.models import Q
@login_required
def inbox(request):
    conversations = Message.get_conversations(user=request.user)
    active_conversation = None
    messages = None
    produituser=Produit.objects.filter(boutique__user_id=request.user.id)
    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['user'].username
        messages = Message.objects.filter(user=request.user,
                                          conversation=conversation['user'])
        messages.update(is_read=True)
        for conversation in conversations:
            if conversation['user'].username == active_conversation:
                conversation['unread'] = 0

    return render(request, 'messenger/inbox.html', {
        'produituser':produituser,
        'messages': messages,
        'conversations': conversations,
        'active': active_conversation
        })


@login_required
def messages(request, username):
    conversations = Message.get_conversations(user=request.user)
    active_conversation = username
    messages = Message.objects.filter(user=request.user,
                                        conversation__username=username)
    messages.update(is_read=True)
    
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0

    boutique_use=request.GET.get('too')
    if not Utilisateur.objects.filter(user=request.user).exists():
        produituser= Produit.objects.filter(boutique__user__username=boutique_use)
        return render(request,'messenger/inbox.html',{'messages': messages,'active': active_conversation,'conversations': conversations,'produituser':produituser})
    else:
        produituser=Produit.objects.filter(boutique__user__username=request.user)
        return render(request,'messenger/inbox.html',{'messages': messages,'active': active_conversation,'conversations': conversations,'produituser':produituser})

    

  


def new(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')

    else:

        if request.method == 'POST':
            from_user = request.user
            to_user_username = request.POST.get('to')
            try:
                to_user = User.objects.get(username=to_user_username)

            except Exception:
                try:
                    to_user_username = to_user_username[
                        to_user_username.rfind('(')+1:len(to_user_username)-1]
                    to_user = User.objects.get(username=to_user_username)

                except Exception:
                    return redirect('/messages/new/')

            message = request.POST.get('message')
            objet=request.POST.get('objet')
            url=request.POST.get('url')
            
            if not url:
                produit= None
            else:
                produit=Produit.objects.get(pk=url)

            if len(message.strip()) == 0:
                return redirect('/messages/new/')

            if from_user != to_user:
                Message.send_message(from_user, to_user, message,objet,produit)

            id_boutique=request.GET.get('boutic')
            return redirect('/messages/{0}/?too={1}'.format(to_user_username,to_user_username))

        else:
            id_boutique=request.GET.get('boutic')
            
            conversations = Message.get_conversations(user=request.user)

            if not Utilisateur.objects.filter(user=request.user).exists():
                produituser= Produit.objects.filter(boutique_id=id_boutique)
                return render(request,'messenger/new.html',{'conversations': conversations,'produituser':produituser})
            else:
                produituser=Produit.objects.filter(boutique__user__username=request.user)
                return render(request,'messenger/new.html',{'conversations': conversations,'produituser':produituser})

            


@login_required
@ajax_required
def delete(request):
    return HttpResponse()


@login_required
@ajax_required
def send(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')

        to_user = User.objects.get(username=to_user_username)
        message = request.POST.get('message')
     
        print("okkkk")
        if len(message.strip()) == 0:
            return HttpResponse()
        if from_user != to_user:
            #form = AttachementForm(request.POST, request.FILES)
            #image = form.save(commit=False)
            msg = Message.send_message(from_user, to_user, message,None,None)
            return render(request, 'messenger/includes/partial_message.html',
                          {'message': msg})

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@login_required
@ajax_required
def users(request):
    users = User.objects.filter(is_active=True)
    dump = []
    template = '{0} ({1})'
    for user in users:
        if user.profile.get_screen_name() != user.username:
            dump.append(template.format(user.profile.get_screen_name(),
                                        user.username))
        else:
            dump.append(user.username)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')


@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)


def search_modal(request):
    boutique_use=request.GET.get('to')
    query = request.GET.get("recherche")
    too= request.GET.get("to")
    print(too)
    
    if not Utilisateur.objects.filter(user=request.user).exists():

        produituser= Produit.objects.filter(boutique__user__username=boutique_use)
        produituser = produituser.filter(
           Q(title__contains=query) | Q(descreption__contains=query)).distinct()
        return render(request,'produit/testt.html',{'produituser':produituser,'too':too})
    else:
        produituser=Produit.objects.filter(boutique__user__username=request.user)
        produituser = produituser.filter(
           Q(title__contains=query) | Q(descreption__contains=query)).distinct()
        return render(request,'produit/testt.html',{'produituser':produituser,'too':too})   

@login_required
@ajax_required
def attache_image(request):
    if request.method == 'POST':
        
        from_user = request.user
        to_user_username = request.POST.get('to1')
        
        to_user = User.objects.get(username=to_user_username)
        form = AttacheForm(request.POST or None,request.FILES or None)
        
        attache = form.save(commit=False)
        msg = Message.send_message(from_user=from_user, to_user=to_user, message=None,objet=None, produit=None)
        attache.message = msg
        
        attache.save()
        
        print("ok!")

        
        to_user_username = request.POST.get('to')
        url=request.POST.get('url')
        id_boutique=request.GET.get('boutic')
        return render(request, 'messenger/includes/partial_message.html',
                            {'message': msg})
    else:
        return HttpResponseBadRequest()


@login_required
@ajax_required
def send2(request):
    if request.method == 'POST':
        
        from_user = request.user
        to_user_username = request.POST.get('to')
        print(to_user_username)
        to_user = User.objects.get(username=to_user_username)
        print(to_user)

        objet=request.POST.get('objet')
        url= request.POST.get('url')
        print(url)
        
        produit=Produit.objects.get(pk=url)
        print(produit.title)

        if from_user != to_user:
            msg = Message.send_message(from_user, to_user, "",objet,produit)
            return render(request, 'messenger/includes/partial_message.html',
                          {'message': msg})
       
    else:
        return HttpResponseBadRequest()  



def new2(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')

    else:

        if request.method == 'POST':
            from_user = request.user
            to_user_username = request.POST.get('to')
            try:
                to_user = User.objects.get(username=to_user_username)

            except Exception:
                try:
                    to_user_username = to_user_username[
                        to_user_username.rfind('(')+1:len(to_user_username)-1]
                    to_user = User.objects.get(username=to_user_username)

                except Exception:
                    return redirect('/messages/new/')

            message = request.POST.get('message')
            objet=request.POST.get('objet')
            url=request.POST.get('url')
            produit=Produit.objects.get(pk=url)
            

            if from_user != to_user:
                Message.send_message(from_user, to_user, message,objet,produit)

            id_boutique=request.GET.get('boutic')
            return redirect('/messages/{0}/?too={1}'.format(to_user_username,to_user_username))

        else:
            id_boutique=request.GET.get('boutic')
            
            conversations = Message.get_conversations(user=request.user)

            if not Utilisateur.objects.filter(user=request.user).exists():
                produituser= Produit.objects.filter(boutique_id=id_boutique)
                return render(request,'messenger/new.html',{'conversations': conversations,'produituser':produituser})
            else:
                produituser=Produit.objects.filter(boutique__user__username=request.user)
                return render(request,'messenger/new.html',{'conversations': conversations,'produituser':produituser})

            
  




