from rest_framework import serializers
from .models import Cliente, Solicitud

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields=('id','nombre','apellido','domicilio','telefono')
class SolicitudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields='__all__'