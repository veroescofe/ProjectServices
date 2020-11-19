from django.shortcuts import render
from apps.repuesto.models import Repuesto
from .resources import RepuestoResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.views.generic import ListView
from .serializers import RepuestoSerializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def simple_upload(request):
    if request.method=='POST':
        repuesto_resource=RepuestoResources()
        dataset=Dataset()
        new_repuesto=request.FILES('archivo')

class RepuestoList(ListView):
    model = Repuesto
    template_name ='repuesto/listado.html'

def listado_repuesto(request):
    
    repuestos=Repuesto.objects.all()
    return render(request,'repuesto/listado.html',{'repuestos':repuestos})

class RepuestoListSerial(APIView):
    def get(self,request):
        repuesto=Repuesto.objects.all()
        serializer=RepuestoSerializers(repuesto,many=True)
        return Response(serializer.data)