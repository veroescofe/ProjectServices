from rest_framework import serializers
from .models import Repuesto

class RepuestoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Repuesto
        fields='__all__'