from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView
from apps.cliente.forms import ClienteForm, SolicitudForm
from django.urls.base import reverse_lazy
from apps.cliente.models import Cliente,Solicitud
from django.http import HttpResponseRedirect

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