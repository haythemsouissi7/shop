from . import views
from django.conf.urls import include, url
from tastypie.api import Api




app_name = 'album'
urlpatterns= [
	

	url(r'^album/(?P<boutique_id>\d+)/$', views.formulaire, name='formulaire'),

	url(r'^create_album/(?P<boutique_id>\d+)/$', views.create_album, name='create_album'),

	url(r'^albums/(?P<boutique_id>\d+)/$', views.albums, name='albums'),
	url(r'^show_picture/(?P<album_id>\d+)/$', views.show_picture, name='show_picture'),

	url(r'^add_picture/(?P<album_id>\d+)/$', views.add_picture, name='add_picture'),



]