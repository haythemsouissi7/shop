from . import views
from django.conf.urls import include, url
from tastypie.api import Api




app_name = 'boutique'
urlpatterns= [

 

    url(r'^create_boutique/$', views.create_boutique, name='create_boutique'),
    url(r'^$', views.index, name='index'),

    url(r'^create/(?P<boutique_id>[0-9]+)/$', views.create_produit, name='create_produit'),
    url(r'^(?P<boutique_id>[0-9]+)/delete_produit/(?P<produit_id>[0-9]+)/$', views.delete_produit,
        name='delete_produit'),
    url(r'^detail/(?P<boutique_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<boutique_id>[0-9]+)/delete_boutique/$', views.delete_boutique, name='delete_boutique'),

    
    


    

    url(r'^activer/(?P<produit_id>[0-9]+)/$', views.Activer, name='activer'),
    url(r'^desactiv/(?P<produit_id>[0-9]+)/$', views.DesActiver, name='desactiver'),
    




    url(r'^duplique/(?P<produit_id>[0-9]+)/$', views.duppliquer_produit, name='duppliquer'),
 
 

    #url(r'^prod/$', views.post_list2, name='post_list2'),



    url(r'^update/(?P<produit_id>[0-9]+)/$', views.post_update, name='modifier'),

    
    
    url(r'^produ/$', views.recherche, name='recherche'),



    



    
    url(r'^users/$', views.users, name='users_searche'),

 

    url(r'^search/$', views.searchproduit, name='searchproduit'),

   
    

    
 

     url(r'^attache_image/$', views.attache_image, name='attache_image'),
  
    url(r'^react/(?P<pk>\d+)/$', views.react, name='react'),
]

