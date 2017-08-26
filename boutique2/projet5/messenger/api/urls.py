
from django.conf.urls import include, url
from django.contrib import admin
from .views import MessageCreateAPIView, MessageProduitCreateAPIView, MessageAllAPIView

urlpatterns= [


 


  url(r'^msg_list/$', MessageAllAPIView.as_view(), name='message_list'),
  url(r'^msg/(?P<username>[^/]+)/$', MessageCreateAPIView.as_view(), name='message'),
  url(r'^msg_produit/(?P<username>[^/]+)/$', MessageProduitCreateAPIView.as_view(), name='message_produit'),
]