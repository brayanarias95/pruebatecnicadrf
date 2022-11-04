from rest_framework import serializers
from app.models import tabla

class tablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tabla
        fields = ['pedido_datetime' , 'lat_recogida' , 'lon_recogida' , 'lat_destino' , 'lon_destino' , 'conductor']