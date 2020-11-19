from django.urls import path
from apps.repuesto.views import RepuestoList,listado_repuesto,RepuestoListSerial

urlpatterns = [
    path('', listado_repuesto,name='listado'),
    path('listado',RepuestoListSerial.as_view()),
]
