
from django.conf.urls import include, url
from django.contrib import admin
from .views import ProductCreateAPIView,ProductDetailAPIView

urlpatterns= [


 

  url(r'^create/$', ProductCreateAPIView.as_view(), name='create'),
  url(r'^detail/(?P<produit_id>[0-9]+)/$', ProductDetailAPIView.as_view(), name='detail'),
]