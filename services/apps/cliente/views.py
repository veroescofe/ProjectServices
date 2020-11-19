from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView
from apps.cliente.forms import ClienteForm, SolicitudForm
from django.urls.base import reverse_lazy
from apps.cliente.models import Cliente,Solicitud
from django.http import HttpResponseRedirect
from .serializers import ClienteSerializers,SolicitudSerializers
from .models import Cliente,Solicitud
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'cliente/cliente_form.html'
    form_class = SolicitudForm
    second_form_class = ClienteForm
    success_url = reverse_lazy('inicio')

    def get_context_data(self,**kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

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
    def get_object(self,pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        cliente=self.get_object(pk)
        serializer=ClienteSerializers(cliente)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        cliente=self.get_object(pk)
        serializer=ClienteSerializers(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        cliente=self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SolicitudList(APIView):

    def get(self,request):
        solicitud=Solicitud.objects.all()
        serializer=SolicitudSerializers(solicitud,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pass