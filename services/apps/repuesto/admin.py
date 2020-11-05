from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from apps.repuesto.models import Repuesto
from .resources import RepuestoResources

# Register your models here.
class RepuestoAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    archivo = ['nombre']
    list_display = ('nombre_repuesto','cantidad','precio')
    resource_class = RepuestoResources


admin.site.register(Repuesto,RepuestoAdmin)

