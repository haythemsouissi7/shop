
from django.conf.urls import include, url
from django.contrib import admin
from .views import ReactCreateAPIView

urlpatterns= [


 

  url(r'^react/(?P<produit_id>[0-9]+)/$', ReactCreateAPIView.as_view(), name='reaction'),
]