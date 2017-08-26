from messenger.models import Message
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from messenger.api.serializer import MessageCreateUpdateSerializer,MessageProduitCreateUpdateSerializer,MessageAllSerializer
from produit.models import Produit
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import (

    CreateAPIView,

    DestroyAPIView,

    ListAPIView,

    RetrieveAPIView,

    RetrieveUpdateAPIView

    )

 

class MessageCreateAPIView(CreateAPIView):

  

    serializer_class = MessageCreateUpdateSerializer

   

 

    def post(self,request,username):
        serializer= MessageCreateUpdateSerializer(data=request.data)
        user = request.user
    
        to_user=User.objects.get(username=username)
        if serializer.is_valid():
            serializer.save(user=user,from_user=user,conversation=to_user)
            serializer.save(user=to_user,from_user=user,conversation=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MessageProduitCreateAPIView(CreateAPIView):

  

    serializer_class = MessageProduitCreateUpdateSerializer

   

 

    def post(self,request,username):
        serializer= MessageProduitCreateUpdateSerializer(data=request.data)
        user = request.user
 
        to_user=User.objects.get(username=username)
        if serializer.is_valid():
            serializer.save(user=user,from_user=user,conversation=to_user)
            serializer.save(user=to_user,from_user=user,conversation=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MessageAllAPIView(ListAPIView):


    serializer_class=MessageAllSerializer
    

    def get(self, request, format=None):
        user=request.user
        message=Message.objects.filter(from_user=user)
        serializer= MessageAllSerializer(message,many=True)
        serializer_data=serializer.data
        custom_data={'message':serializer_data}
        return Response(custom_data)
   
