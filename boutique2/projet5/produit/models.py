import datetime
from django.conf.urls import url
from django.db import models
import json
from django.contrib import admin
from django.db import models
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import Permission, User
from django.conf import settings

class Boutique(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1)
    logo = models.FileField(max_length=250)

    def __str__(self):
        return self.name


now = datetime.datetime.now()
def group_based_upload_to(instance, filename):
    return "image/media/{}/{}/{}/{}".format(instance.boutique.user,instance.boutique.name,instance.title+str(instance.id) ,filename+'-'+str(now))



def group_based_upload_to_seconder(instance, filename):
    return "image//media/ali/secondaire/{}/{}".format(instance.boutique.name, filename)


class Image(models.Model):
    image1 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image2 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image3 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)


class Produit(models.Model):
    etat_choix = (('active', 'active'), ('desactive', 'desactive'),)
    typechoix = (('vintage', 'vintage'), ('fait a la main', 'fait a la main'),)
    choix_categorie = (
    ('bijoux ', 'bijoux '), ('maison et ameublement', 'maison et ameublement'), ('vetements ', 'vetements '),
    ('art et collections', 'art et collections'), ('accessoires ', 'accessoires '),
    ('sacs et bagages', 'sacs et bagages'), ('mariage ', 'mariage '),)
    prix = models.IntegerField()
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250,choices=typechoix, default="vintage")
    etat = models.CharField(max_length=250, choices=etat_choix, default="desactive")
    descreption = models.CharField(max_length=250)
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=group_based_upload_to)
    image1 = models.ImageField(upload_to=group_based_upload_to, default=None, blank=True)
    image2 = models.ImageField(upload_to=group_based_upload_to, default=None,blank=True)
    image3 = models.ImageField(upload_to=group_based_upload_to, default=None,blank=True)
    categorie = models.CharField(max_length=250, choices=choix_categorie, default='bijoux')
    dat = models.DateTimeField(auto_now_add=True, null=True)
    quantite = models.IntegerField(default=None)
    
    def get_prix(self):
        return self.prix


    def get_likers(self):
        
        likers = []
        for like in self.likers:
            likers.append(like.user)
        return likers

    def get_normal(self):
        return self.reaction_set.filter(type= 'normal').count()

    def get_smile(self):
        return self.reaction_set.filter(type= 'smile').count()

    def get_love(self):
        return self.reaction_set.filter(type= 'love').count()

    def get_wish(self):
        return self.reaction_set.filter(type= 'wish').count()
    def get_number(self):
        return self.reaction_set.count() 


    def __str__(self):
        return self.title + ' - ' + str(self.prix)







class Like(models.Model):
    user=models.ForeignKey(User, null=True)
    produit=models.ForeignKey(Produit,null=True)
    type = models.CharField(max_length=255, blank=True, null=True, choices=(('NORMAL', 'normal'), ('SMILE', 'smile'), ('LOVE', 'love'), ('WISH', 'wish'),))
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = (('user', 'produit'),)

    @staticmethod
    def get_choices():
        return [choice[1] for choice in Like._meta.get_field('type').choices]

class Love(models.Model):
    user=models.ForeignKey(User, null=True)
    produit=models.ForeignKey(Produit,null=True)
    
