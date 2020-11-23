from django.shortcuts import render
from apps.reparacion.models import Reparacion,DetalleReparacion
from .serializers import ReparacionSerializers,DetalleReparacionSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class ReparacionList(APIView):
    def get(self,request):
        reparacion=Reparacion.objects.all()
        serializer=ReparacionSerializers(reparacion,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ReparacionSerializers(data=request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ReparacionDetail(APIView):
    def get(self,request,pk):
        reparacion=Reparacion.objects.filter(id=pk)
        serializer=ReparacionSerializers(reparacion,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        reparacion=Reparacion.objects.all(pk=pk)
        serializer=ReparacionSerializers(reparacion,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        reparacion=Reparacion.objects.get(pk=pk)
        reparacion.delete()
        return Response(status=status.HTTP_204_NO_CONTEN)
class DetalleReparacionList(APIView):
    def get(self,request):
        detalle=DetalleReparacion.objects.all()
        serializer=DetalleReparacionSerializers(detalle,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=DetalleReparacionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DetalleReparacionDetail(APIView):
    def get(self,request,pk):
        detalle=DetalleReparacion.objects.filter(id=pk)
        serializer=DetalleReparacionSerializers(detalle,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        detalle=DetalleReparacion.objects.get(pk=pk)
        serializer=DetalleReparacionSerializers(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        detalle=DetalleReparacion.objects.all(pk=pk)
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
