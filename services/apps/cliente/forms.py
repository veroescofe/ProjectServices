from django import forms
from apps.cliente.models import Cliente,Solicitud

from django.forms.models import inlineformset_factory

'''SolicitudFormset = inlineformset_factory(
    Cliente,
    Solicitud ,
    fields=('fecha','marca','falla','cliente'),
    extra=1
)'''

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','domicilio','telefono']
    
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['fecha','marca','falla']
        