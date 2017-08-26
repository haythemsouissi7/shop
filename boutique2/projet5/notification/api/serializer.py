from notification.models import Notification
from rest_framework.serializers import ModelSerializer, SerializerMethodField


from rest_framework.serializers import ModelSerializer

 

class NotificationSerializer(ModelSerializer):

    class Meta:

        model = Notification

        fields = ['id', 'product', 'is_read','type','date'

          

        ]  
