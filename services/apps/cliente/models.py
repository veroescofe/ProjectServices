from django.db import models

# Create your models here.

class Cliente(models.Model):
    '''Modelo para el cliente'''
    nombre=models.CharField(max_length=30,null=False,verbose_name='Nombre')
    apellido=models.CharField(max_length=30,null=False,verbose_name='Apellido')
    domicilio=models.CharField(max_length=70,null=False,verbose_name='Domicilio')
    telefono=models.CharField(max_length=15,null=False,verbose_name='Telefono')
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
        
class Solicitud(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cliente')
    fecha=models.DateField(verbose_name='Fecha de visita')
    marca=models.CharField(max_length=20,null=False,verbose_name='Marca del lavarropas')
    falla=models.CharField(max_length=50,null=False,verbose_name='Falla del lavarropas')
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cliente: {} {},Domicilio: {}, Fecha de visita: {}".format(self.cliente.nombre,self.cliente.apellido,self.cliente.domicilio, self.fecha)

    class Meta:
        db_table = 'solicitud'
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['id']