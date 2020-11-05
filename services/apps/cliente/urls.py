from django.urls import path
from apps.cliente.views import SolicitudCreate


urlpatterns = [
    path('solicitud/', SolicitudCreate.as_view(),name='solicitud'),
]