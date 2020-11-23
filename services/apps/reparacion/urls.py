from django.urls import path
from apps.reparacion.views import (
    ReparacionList,
    ReparacionDetail,
    DetalleReparacionList,
    DetalleReparacionDetail,
)


urlpatterns = [
    path('reparacion/', ReparacionList.as_view()),
    path('reparacion/<int:pk>', ReparacionDetail.as_view()),
    path('detalle/', DetalleReparacionList.as_view()),
    path('detalle/<int:pk>', DetalleReparacionDetail.as_view()),
]