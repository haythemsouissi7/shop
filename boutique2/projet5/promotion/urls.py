from . import views
from django.conf.urls import include, url
from tastypie.api import Api




app_name = 'promotion'
urlpatterns= [

 
    url(r'^form/$', views.formpromotion, name='formulaire'),
    url(r'^form_failed/$', views.formpromotion_failed, name='formulaire_failed'),
    url(r'^form_failed_collection/$', views.formpromotion_failed_collection, name='formulaire_failed_collection'),
    url(r'^create_promotion/$', views.create_promotion, name='create_promotion'),
    url(r'^get_collection/$', views.get_collection, name='get_collection'),
    url(r'^promotions/(?P<boutique_id>[0-9]+)/$', views.promotions, name='promotions'),
 	url(r'^time/(?P<promotion_id>[0-9]+)/$', views.get_Datas, name='get_Datas'),

    
]

