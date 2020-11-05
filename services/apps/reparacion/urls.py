from django.urls import path
from apps.reparacion.views import DetalleCreate


urlpatterns = [
    path('', DetalleCreate.as_view(),name='reparacion'),
]