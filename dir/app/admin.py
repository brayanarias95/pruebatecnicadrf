from django.contrib import admin
from app.models import tabla
# Register your models here.
@admin.register(tabla)
class tablaAdmin(admin.ModelAdmin):
    list_display = ['pedido_datetime' , 'lat_recogida' , 'lon_recogida' , 'lat_destino' , 'lon_destino' , 'conductor']
