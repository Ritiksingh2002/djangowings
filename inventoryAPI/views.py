from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ViewSet ):
    def list(self,request):
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)






