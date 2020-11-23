from django.urls import path
from apps.repuesto.views import (
    RepuestoList,
    RepuestoDetail,
)

urlpatterns = [
    path('listado/',RepuestoList.as_view()),
    path('detalleRepuesto/<int:pk>',RepuestoDetail.as_view()),
]
