from django.db import models

# Create your models here.
import datetime
from django.conf.urls import url
from django.db import models
import json
from django.contrib import admin
# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseBadRequest
# Create your models here.
from django.contrib.auth.models import Permission, User
from django.db import models
from django.conf import settings
from produit.models import Produit
class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True, null=True, choices=(('NORMAL', 'normal'), ('SMILE', 'smile'), ('LOVE', 'love'), ('WISH', 'wish'),))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'product'),)

    @staticmethod
    def get_choices():
        return [choice[1] for choice in Reaction._meta.get_field('type').choices]