from produit.models import Produit,Boutique
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from produit.api.serializer import ProductCreateUpdateSerializer,ProductDetailSerializer

from rest_framework.generics import (

    CreateAPIView,

    DestroyAPIView,

    ListAPIView,

    RetrieveAPIView,

    RetrieveUpdateAPIView

    )

 

class ProductCreateAPIView(CreateAPIView):

    queryset = Produit.objects.all()

    serializer_class = ProductCreateUpdateSerializer

   

 

    def perform_create(self, serializer):

        user = self.request.user

       

        boutique=Boutique.objects.filter(user=user)

        serializer.save(boutique=boutique[0])









class ProductDetailAPIView(CreateAPIView):

    queryset = Produit.objects.all()
    serializer_class=ProductDetailSerializer
    

    def get(self, request,produit_id, format=None):

    	produit= Produit.objects.get(pk=produit_id)
    	serializer= ProductDetailSerializer(produit)
    	serializer_data=serializer.data
    	custom_data={'produit':serializer_data}
    	return Response(custom_data)
   










