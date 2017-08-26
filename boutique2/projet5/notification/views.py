from django.shortcuts import render

# Create your views here.
import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from projet5.decorators import ajax_required

from .models import Notification
from produit.models import Produit

@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)
    unread = Notification.objects.filter(to_user=user, is_read=False)
    for notification in unread:
        notification.is_read = True
        notification.save()

    return render(request, 'notification/notifications.html',
                  {'notifications': notifications})


@login_required
@ajax_required
def last_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user,
                                                is_read=False)[:5]
    print(notifications)
    for notification in notifications:
        notification.is_read = True
        notification.save()

    return render(request,
                  'notification/last_notifications.html',
                  {'notifications': notifications})


@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user,
                                                is_read=False)[:5]
    return HttpResponse(len(notifications))
