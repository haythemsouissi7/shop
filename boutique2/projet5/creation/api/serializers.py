from produit.models import Produit
from rest_framework.serializers import ModelSerializer, SerializerMethodField
class ProductListSerializer(ModelSerializer):
	class Meta:
		model=Produit
		fields=('id','prix', 'title', 'descreption', 'type', 'etat', 'categorie','dat','quantite')



