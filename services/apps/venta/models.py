from django.db import models
from apps.repuesto.models import Repuesto
from apps.cliente.models import Cliente

# Create your models here.

class DetalleVenta(models.Model):
    repuesto=models.ManyToManyField(Repuesto,verbose_name='Repuestos')
    cantidad=models.IntegerField(verbose_name='Cantidad de repuestos')
    subtotal=models.IntegerField(verbose_name='Subtotal a pagar')

    def __str__(self):
        return f'Detalle n°: {self.id},Subtotal: ${self.subtotal}'

    class Meta:
        db_table='detalleventa'
        verbose_name='Detalle'
        verbose_name_plural='Detalles'
        ordering=['id']

class Venta(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    detalle=models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, verbose_name='Detalles de venta')
    fecha=models.DateField(auto_now_add=True, verbose_name='Fecha de venta')

    modopago=(
        ('efectivo','Efectivo'),
        ('debito','Tarjeta de debito'),
        ('credito','Tarjeta de credito'),
    )
    formapago=models.CharField(max_length=20, choices=modopago,verbose_name='Forma de pago')
    total=models.IntegerField(verbose_name='Total a pagar')

    def __str__(self):
        return self.cliente.nombre

    class Meta:
        db_table='venta'
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        ordering=['id']
