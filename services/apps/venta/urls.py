from django.urls import path
from apps.venta.views import VentaList,DetalleVentaList

urlpatterns = [
    path('', VentaList.as_view()),
    path('detalleventa/',DetalleVentaList.as_view()),
]
