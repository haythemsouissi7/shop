from django.conf.urls import url

from django.contrib import admin
from .views import ProductList

urlpatterns= [


	url(r'^$', ProductList.as_view(), name='list'),

]