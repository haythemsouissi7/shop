from . import views
from django.conf.urls import include, url
from django.contrib import admin
app_name = 'settings'

urlpatterns= [


  url(r'^profile/$', views.profile_user, name='profile'),
]