from django.contrib import admin
from apps.reparacion.models import Reparacion,DetalleReparacion

# Register your models here.

admin.site.register(Reparacion)
admin.site.register(DetalleReparacion)