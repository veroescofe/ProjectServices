from django.urls import path
from apps.repuesto.views import RepuestoList,listado_repuesto


urlpatterns = [
    path('', listado_repuesto,name='listado'),
]