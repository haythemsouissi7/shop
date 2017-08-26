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




now = datetime.datetime.now()
def group_based_upload_to(instance, filename):
    return "image/media/{}/{}/{}".format(instance.album.user,instance.album.name,filename+'-'+str(now))



def group_based_upload_to_seconder(instance, filename):
    return "image//media/ali/secondaire/{}/{}/{}".format(instance.user, instance.name,filename)

class Album(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1)
    image = models.ImageField(upload_to=group_based_upload_to_seconder,null=True)
    def __str__(self):
        return self.name


class Picture(models.Model):
    
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name='+')
    logo = models.ImageField(upload_to=group_based_upload_to)
    dat = models.DateTimeField(auto_now_add=True, null=True)

 







    