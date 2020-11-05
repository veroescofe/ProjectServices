from django.views.generic import CreateView,ListView,DeleteView
from apps.reparacion.forms import ReparacionForm,DetalleRepForm
from django.urls.base import reverse_lazy
from apps.reparacion.models import Reparacion,DetalleReparacion
from django.http import HttpResponseRedirect


class DetalleCreate(CreateView):
    model=DetalleReparacion
    template_name='reparacion/reparacion_form.html'
    form_class=DetalleRepForm
    second_form_class=ReparacionForm
    success_url=reverse_lazy('reparacion')

    def get_context_data(self, **kwargs):
        context=super(DetalleCreate,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2']=self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST)
        form2=self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            reparacion=form2.save()
            reparacion.detalle_reparacion=form.save()
            reparacion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))