from django.shortcuts import render
from apps.repuesto.models import Repuesto
from .resources import RepuestoResources
from tablib import Dataset
from .serializers import RepuestoSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def simple_upload(request):
    if request.method=='POST':
        repuesto_resource=RepuestoResources()
        dataset=Dataset()
        new_repuesto=request.FILES('archivo')

class RepuestoList(APIView):
    def get(self,request):
        repuesto=Repuesto.objects.all()
        serializer=RepuestoSerializers(repuesto,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=RepuestoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class RepuestoDetail(APIView):
    def get(self,request,pk):
        repuesto=Repuesto.objects.filter(id=pk)
        serializer=RepuestoSerializers(repuesto,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        repuesto=Repuesto.objects.get(pk=pk)
        serializer=RepuestoSerializers(repuesto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        repuesto=Repuesto.objects.all(pk=pk)
        repuesto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
