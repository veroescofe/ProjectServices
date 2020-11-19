from rest_framework import serializers
from .models import Venta, DetalleVenta

class VentaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Venta
        fields='__all__'

class DetalleVentaSerializers(serializers.ModelSerializer):
    class Meta:
        model=DetalleVenta
        fields='__all__'