from django.urls import path
from apps.reparacion.views import DetalleCreate,ReparacionList,DetalleReparacionList


urlpatterns = [
    path('', DetalleCreate.as_view(),name='reparacion'),
    path('reparacion/', ReparacionList.as_view()),
    path('detallereparacion/', DetalleReparacionList.as_view()),
]