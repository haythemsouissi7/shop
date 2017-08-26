from reaction.models import Reaction
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from reaction.api.serializer import ReactCreateUpdateSerializer
from produit.models import Produit
from rest_framework import status
from rest_framework.generics import (

    CreateAPIView,

    DestroyAPIView,

    ListAPIView,

    RetrieveAPIView,

    RetrieveUpdateAPIView

    )

 

class ReactCreateAPIView(CreateAPIView):

  

    serializer_class = ReactCreateUpdateSerializer

   

 

    def post(self,request,produit_id):
        serializer= ReactCreateUpdateSerializer(data=request.data)
        user = request.user
        produit=Produit.objects.get(pk=produit_id)
        if serializer.is_valid():
            try:
                reaction = Reaction.objects.get(user=request.user , product=produit)
                if reaction.type == serializer.validated_data['type']:
                    reaction.delete()
                    
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    serializer.save(user=request.user,product=produit)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Reaction.DoesNotExist:
                serializer.save(user=request.user,product=produit)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

               


