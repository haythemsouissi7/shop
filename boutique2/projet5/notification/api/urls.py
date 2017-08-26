
from django.conf.urls import include, url
from django.contrib import admin
from .views import NotificationDetailAPIView

urlpatterns= [


  url(r'^notif/(?P<username>[^/]+)/$', NotificationDetailAPIView.as_view(), name='all_notif'),
]