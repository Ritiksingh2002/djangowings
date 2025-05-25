from django.shortcuts import render


from rest_framework import viewsets
from .models import CreateBook
from .serializers import CreateBookSerializer


class CreateBookViewSet(viewsets.ModelViewSet):
    queryset= CreateBook.objects.all()
    serializer_class= CreateBookSerializer
