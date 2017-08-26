from . import views
from django.conf.urls import include, url
from tastypie.api import Api




app_name = 'discover'
urlpatterns= [
	
    url(r'^aa/(?P<boutique_id>[0-9]+)/$', views.post_list3, name='post_produit3'),
	url(r'^visite/(?P<boutique_id>[0-9]+)/$', views.visite_boutique, name='visite_boutique'),
    url(r'^vosproduit/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_produit'),
    
    url(r'^produit/(?P<produit_id>[0-9]+)/$', views.Detail0, name='detail_produitdescover'),
	url(r'^produits/$', views.post_list, name='post_list'),
	url(r'^produits1/$', views.filter2, name='filter2'),



]