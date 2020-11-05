from django.db import models
from apps.cliente.models import Solicitud
from apps.repuesto.models import Repuesto

# Create your models here.

class DetalleReparacion(models.Model):
    repuesto=models.ManyToManyField(Repuesto,verbose_name='Reparaciones')
    
    def __str__(self):
        return "N°: {}".format(self.id)

    class Meta:
        db_table = 'detallereparacion'
        verbose_name ='Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['id']

        
class Reparacion(models.Model):
    solicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=True,blank=True,verbose_name='Cliente')
    detalle_reparacion=models.ForeignKey(DetalleReparacion,on_delete=models.CASCADE, null=True,blank=True,verbose_name='Detalle de reparacion')
    fecha_entrega=models.DateField(verbose_name='Fecha de entrega(aprox)')
    precio=models.CharField(max_length=6,verbose_name='Precio')

    def __str__(self):
        return "Cliente: {} {}, Precio: ${}".format(self.solicitud.cliente.nombre,self.solicitud.cliente.apellido, self.precio)

    class Meta:
        db_table = 'reparacion'
        verbose_name ='Reparacion'
        verbose_name_plural = 'Reparaciones'
        ordering = ['id']


    