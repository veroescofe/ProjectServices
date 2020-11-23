from django.urls import path
from apps.venta.views import (
    VentaList,
    VentaDetail,
    DetalleVentaList,
    DetalleVentaDetail,
)

urlpatterns = [
    path('venta/', VentaList.as_view()),
    path('venta/<int:pk>', VentaDetail.as_view()),
    path('detalleventa/',DetalleVentaList.as_view()),
    path('detalleventa/<int:pk>',DetalleVentaDetail.as_view()),
]
