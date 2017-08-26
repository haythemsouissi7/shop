from django.db import models
from django.conf.urls import url
import datetime
# Create your models here.
from authentication.models import Utilisateur
from produit.models import Produit
from django.conf import settings
from django.contrib.auth.models import Permission, User
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

now = datetime.datetime.now()
def group_based_upload_to(instance, filename):
    return "image/media/{}/{}/{}".format(instance.owner,instance.title+str(instance.id) ,filename+'-'+str(now))




class Collection(models.Model):
	owner= models.ForeignKey(User,on_delete=models.CASCADE)
	produit=models.ManyToManyField(Produit,blank=True)
	title= models.CharField(max_length=250)
	discription= models.CharField(max_length=250)
	is_active=models.BooleanField(default = False)
	created_at=models.DateTimeField(auto_now_add=True, null=True)
	picture=models.ImageField(upload_to=group_based_upload_to, default=None, blank=True)
	

