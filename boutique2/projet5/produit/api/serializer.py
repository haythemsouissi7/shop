from produit.models import Produit
from rest_framework.serializers import ModelSerializer, SerializerMethodField


from rest_framework.serializers import ModelSerializer

 

class ProductCreateUpdateSerializer(ModelSerializer):

    class Meta:

        model = Produit

        fields = ['prix', 'title', 'descreption', 'type', 'etat', 'categorie','dat','quantite','logo'

          

        ]  




class ProductDetailSerializer(ModelSerializer):

    class Meta:

        model = Produit

        fields = ['id','prix', 'title', 'descreption', 'type', 'etat', 'categorie','dat','quantite','logo'

          

        ]  









