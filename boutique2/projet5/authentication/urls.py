from . import views
from django.conf.urls import include, url
from tastypie.api import Api



app_name = 'authontication'
urlpatterns= [



	url(r'^login_users/bb/$', views.login_descover, name='login_descover'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^business_register/$', views.utilisateur_register, name='business_register'),
]