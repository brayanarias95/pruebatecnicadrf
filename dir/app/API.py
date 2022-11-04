import imp
from app.models import tabla
from rest_framework import viewsets, permissions
from app.serializers import tablaSerializer

class appViewSet(viewsets.ModelViewSet):
    queryset = tabla.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class= tablaSerializer