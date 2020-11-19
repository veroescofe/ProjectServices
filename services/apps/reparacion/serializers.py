from rest_framework import serializers
from .models import Reparacion,DetalleReparacion

class ReparacionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reparacion
        fields='__all__'

class DetalleReparacionSerializers(serializers.ModelSerializer):
    class Meta:
        model=DetalleReparacion
        fields='__all__'