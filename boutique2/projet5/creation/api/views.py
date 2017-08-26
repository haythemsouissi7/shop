from produit.models import Produit
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from creation.api.serializers import ProductListSerializer
class ProductList(ListAPIView):
	queryset=Produit.objects.filter(etat="active")
	def get(self, request, format=None):
		products= Produit.objects.filter(etat="active")
		serializer= ProductListSerializer(products,many=True)
		return Response(serializer.data)