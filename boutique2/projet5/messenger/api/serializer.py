from messenger.models import Message
from rest_framework.serializers import ModelSerializer, SerializerMethodField


from rest_framework.serializers import ModelSerializer

 

class MessageCreateUpdateSerializer(ModelSerializer):

    class Meta:

        model = Message

        fields = ['message','is_read','date'
          

        ]  



class MessageProduitCreateUpdateSerializer(ModelSerializer):

    class Meta:

        model = Message

        fields = ['message','is_read','date','produit'
          

        ]  



class MessageAllSerializer(ModelSerializer):

    class Meta:

        model = Message

        fields = ['id','message','is_read','date'

          

        ]  









