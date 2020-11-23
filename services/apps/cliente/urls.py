from django.urls import path
from apps.cliente.views import (
    ClienteList,
    ClienteDetail,
    SolicitudList,
    SolicitudDetail,
    )

urlpatterns = [
    path('cliente/', ClienteList.as_view()),
    path('cliente/<int:pk>', ClienteDetail.as_view()),
    path('lista/', SolicitudList.as_view()),
    path('solicitud/<int:pk>', SolicitudDetail.as_view()),
]
