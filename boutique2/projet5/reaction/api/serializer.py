from reaction.models import Reaction
from rest_framework.serializers import ModelSerializer, SerializerMethodField


from rest_framework.serializers import ModelSerializer

 

class ReactCreateUpdateSerializer(ModelSerializer):

    class Meta:

        model = Reaction

        fields = ['type'
          

        ]  







