from django import forms
from apps.reparacion.models import Reparacion, DetalleReparacion

class ReparacionForm(forms.ModelForm):
    class Meta:
        model=Reparacion
        fields=['solicitud','fecha_entrega','precio']
        

class DetalleRepForm(forms.ModelForm):
    class Meta:
        model=DetalleReparacion
        fields=['repuesto']

        widgets={'repuesto':forms.CheckboxSelectMultiple()}