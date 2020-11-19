from django.contrib import admin
from apps.venta.models import Venta, DetalleVenta

# Register your models here.

admin.site.register(Venta)
admin.site.register(DetalleVenta)