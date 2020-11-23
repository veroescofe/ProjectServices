from django.shortcuts import render
from apps.cliente.models import Cliente,Solicitud
from .serializers import ClienteSerializers,SolicitudSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class ClienteList(APIView):
    def get(self,request):
        cliente=Cliente.objects.all()
        serializer=ClienteSerializers(cliente,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ClienteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ClienteDetail(APIView):
    def get(self,request,pk,format=None):
        cliente=Cliente.objects.filter(id=pk)
        serializer=ClienteSerializers(cliente, many=True)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        cliente=Cliente.objects.get(pk=pk)
        serializer=ClienteSerializers(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        cliente=Cliente.objects.get(pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SolicitudList(APIView):
    def get(self,request):
        solicitud=Solicitud.objects.all()
        serializer=SolicitudSerializers(solicitud,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=SolicitudSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SolicitudDetail(APIView):
    def get(self,request,pk):
        solicitud=Solicitud.objects.filter(id=pk)
        sereializer=SolicitudSerializers(solicitud,many=True)
        return Response(sereializer.data)

    def put(self,request,pk):
        solicitud=Solicitud.objects.get(pk=pk)
        serializer=SolicitudSerializers(solicitud,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        solicitud=Solicitud.objects.get(pk=pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)