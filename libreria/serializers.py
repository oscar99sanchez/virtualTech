from dataclasses import field
from rest_framework import serializers
from .models import Mouses

class MousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouses
        field = ('id', 'categorias', 'producto', 'img', 'precio')
        