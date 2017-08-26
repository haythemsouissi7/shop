from . import views
from django.conf.urls import include, url
from tastypie.api import Api




app_name = 'collection'
urlpatterns= [
	

	url(r'^detail/(?P<collection_id>\d+)/$', views.detail_collection, name='detail_collection'),

	url(r'^creat_col/$', views.formulaire_collection, name='formulaire_collection'),
	url(r'^edit/(?P<collection_id>\d+)/$', views.edit_collection, name='edit_collection'),
	url(r'^update/(?P<collection_id>\d+)/$', views.edit, name='edit'),
	url(r'^update_image/(?P<collection_id>\d+)/$', views.edit_image, name='edit_image'),
	url(r'^active/(?P<collection_id>\d+)/$', views.active, name='active'),
	




]