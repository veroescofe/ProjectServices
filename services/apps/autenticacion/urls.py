from django.urls import path
from apps.autenticacion.views import VistaRegistro,index,salir,acceder,UserApi

urlpatterns = [
    path('',index,name='inicio'),
    path('registro/',VistaRegistro.as_view(),name='registro'),
    path('salir/',salir,name='salir'),
    path('acceder/',acceder,name='acceder'),
    path('user/',UserApi.as_view()),
]