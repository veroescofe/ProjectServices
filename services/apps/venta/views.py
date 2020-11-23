from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import Venta,DetalleVenta
from .serializers import VentaSerializers,DetalleVentaSerializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class VentaList(APIView):
    def get(self,request):
        venta=Venta.objects.all()
        serializer=VentaSerializers(venta,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=VentaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class VentaDetail(APIView):
    def get(self,request,pk):
        venta=Venta.objects.filter(id=pk)
        serializer=VentaSerializers(venta,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        venta=Venta.objects.get(pk=pk)
        serializer=VentaSerializers(venta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        venta=Venta.objects.all(pk=pk)
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetalleVentaList(APIView):
    def get(self,request):
        detalle=DetalleVenta.objects.all()
        serializer=DetalleVentaSerializers(detalle,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=DetalleVentaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DetalleVentaDetail(APIView):
    def get(self,request,pk):
        detalle=DetalleVenta.objects.filter(id=pk)
        serializer=DetalleVentaSerializers(detalle,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        detalle=DetalleVenta.objects.get(pk=pk)
        serializer=DetalleVentaSerializers(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        detalle=DetalleVenta.objects.all(pk=pk)
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
