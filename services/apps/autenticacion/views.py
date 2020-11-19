from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from .serializers import UserSerializers
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

def index(request):
    return render(request,'index.html')

def acceder(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data('username')
            password=form.cleaned_data('password')
            usuario=authenticate(usernaem=nombre_usuario, password=password)
            if usuario is not None:
                login(request,usuario)
                messages.success(request, F'Bienvenido/a')
                return redirect('inicio')
            else:
                messages.error(request, 'Los datos son incorrectos')
        else:
            messages.error(request,'Los datos son incorrectos')
    form=AuthenticationForm()
    return render(request,'acceder.html',{'form':form})
    
class VistaRegistro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,'registro.html',{'form':form})

    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            nombre_usuario=form.cleaned_data.get('username')
            messages.success(request, F'Bienvenid@ a la plataforma {nombre_usuario}')
            login(request,usuario)
            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,'registro.html',{'form':form})

def salir(request):
    logout(request)
    messages.success(request, F'Tu sesión se ha cerrado correctamente')
    return redirect('acceder')

class UserApi(APIView):
    def get(self,request,format=None):
        lista=User.objects.all()
        serializer=UserSerializers(lista,many=True)
        return Response(serializer.data)
