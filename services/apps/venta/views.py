from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import Venta,DetalleVenta
from .serializers import VentaSerializers,DetalleVentaSerializers
from rest_framework.response import Response

# Create your views here.

class VentaList(APIView):
    def get(self,request):
        venta=Venta.objects.all()
        serializer=VentaSerializers(venta,many=True)
        return Response(serializer.data)

class DetalleVentaList(APIView):
    def get(self,request):
        detalle=DetalleVenta.objects.all()
        serializer=DetalleVentaSerializers(detalle,many=True)
        return Response(serializer.data)