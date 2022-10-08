from .models import Mouses
from rest_framework import viewsets, permissions
from serializers import MousesSerializer

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouses.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MousesSerializer