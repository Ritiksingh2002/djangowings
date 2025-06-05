from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet ):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permissions_classes=[IsAuthenticated]
    def list(self,request):
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    #POST REQUEST 
    def create(self,request): 
        serializer= ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            item= Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({"detail:":"ITem not found "},status=status.HTTP_400_BAD_REQUEST)
        serializer=ItemSerializer(item,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def Destroy(self,request,pk=None):
        try :
            item=Item.objects.get(pk=pk)
            item.delete()
            return Response([],status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response({"details":"item not found"},status=status.HTTP_400_BAD_REQUEST)







