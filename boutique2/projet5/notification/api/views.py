from notification.models import Notification
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from notification.api.serializer import NotificationSerializer
from django.contrib.auth.models import User
from rest_framework.generics import (

   

    ListAPIView,

  

    )

 







class NotificationDetailAPIView(ListAPIView):

  
    serializer_class=NotificationSerializer
    

    def get(self, request,username, format=None):
        user=User.objects.get(username=username)
        notification= Notification.objects.filter(from_user=user)
        serializer= NotificationSerializer(notification,many=True)
        serializer_data=serializer.data
        custom_data={'notification':serializer_data}
        return Response(custom_data)
   










