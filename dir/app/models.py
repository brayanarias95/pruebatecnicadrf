from django.db import models

# Create your models here.

class tabla(models.Model):
    pedido_datetime = models.DateTimeField()
    lat_recogida = models.IntegerField()
    lon_recogida = models.IntegerField()
    lat_destino = models.IntegerField()
    lon_destino = models.IntegerField()
    conductor = models.IntegerField()
    
