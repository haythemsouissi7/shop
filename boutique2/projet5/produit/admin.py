from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from messenger.models import Message
from django.contrib import admin
from .models import Boutique, Produit
from authentication.models import Utilisateur 
from reaction.models import Reaction
from collection.models import Collection
from promotion.models import Promotion
from album.models import Album,Picture
# Register your models here.
admin.site.register(Boutique)
admin.site.register(Produit)
admin.site.register(Utilisateur)
admin.site.register(Reaction)
admin.site.register(Collection)
admin.site.register(Album)
admin.site.register(Picture)
admin.site.register(Promotion)
admin.site.register(Message)