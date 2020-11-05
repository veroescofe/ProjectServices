from django.db import models

# Create your models here.

class Repuesto(models.Model):
    ''' Modelos para el stock de repuestos'''
    nombre_repuesto=models.CharField(max_length=30, null=False,blank=False,verbose_name='Nombre del Repuesto')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    precio=models.IntegerField(verbose_name='Precio')
    imagen=models.ImageField(upload_to='Repuesto', verbose_name='Imagen del repuesto')

    def __str__(self):
        return "Repuesto: {},Precio: ${}".format(self.nombre_repuesto,self.precio)

    class Meta:
        db_table = 'repuesto'
        verbose_name = 'Repuesto'
        verbose_name_plural = 'Repuestos'
        ordering = ['id']