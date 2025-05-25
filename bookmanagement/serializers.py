from rest_framework import serializers
from .models import CreateBook

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=CreateBook
        fields='__all__'