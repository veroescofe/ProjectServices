from django.urls import path
from apps.cliente.views import SolicitudCreate,ClienteList,ClienteDetail,SolicitudList



urlpatterns = [
    path('solicitud/', SolicitudCreate.as_view(),name='solicitud'),
    path('cliente/', ClienteList.as_view()),
    path('cliente/<int:pk>', ClienteDetail.as_view()),
    path('lista/', SolicitudList.as_view()),
]
