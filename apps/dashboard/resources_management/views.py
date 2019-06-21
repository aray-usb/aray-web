from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import (
    CreateView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from utils.mixins.datatablesmixin import JQueryDataTablesMixin
from apps.api.models import Recurso
from .forms import *


class ResourcesIndexView(TemplateView):
    template_name = 'dashboard/resources_management/resources_management.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
        if Recurso.objects.filter(tipo=0).count() == 0:
            cantMedicinas = 0
        else:
            cantMedicinas = Recurso.objects.get(tipo=0).cantidad
        if  Recurso.objects.filter(tipo=1).count() == 0:
            cantAlimentacion = 0
        else:
            cantAlimentacion = Recurso.objects.get(tipo=1).cantidad
        if Recurso.objects.filter(tipo=2).count() == 0:
            cantTransporte = 0
        else:
            cantTransporte = Recurso.objects.get(tipo=2).cantidad
        if Recurso.objects.filter(tipo=3).count() == 0:    
            cantArticuloRescate = 0
        else:
            cantArticuloRescate = Recurso.objects.get(tipo=3).cantidad
        if Recurso.objects.filter(tipo=4).count() == 0:
            cantOtro = 0
        else:
            cantOtro = Recurso.objects.get(tipo=4).cantidad
        total = cantMedicinas + cantAlimentacion + cantTransporte + cantArticuloRescate + cantOtro
        print(total)
        """
        context["recursos"] =  Recurso.objects.all()
        """
        context['propMedicinas'] = str((cantMedicinas * 100) / total)
        context['propAlimentos'] = str((cantAlimentacion * 100) / total)
        context['propTransporte'] = str((cantTransporte * 100) / total)
        context['propArticuloRescate'] = str((cantArticuloRescate * 100) / total)
        context['propOtro'] = str((cantOtro * 100) / total)
        context['total'] = total
        """
        
        return context

class ResourceCreateView(CreateView):
    form_class = ResourceForm
    model = Recurso
    queryset = Recurso.objects.all()
    template_name = 'dashboard/resources_management/create_resource.html'
    success_url = reverse_lazy('dashboard:resources_management:resources_index')

class ResourceDeleteView(DeleteView):
    context_object_name = 'recurso'
    model = Recurso
    template_name = 'dashboard/resources_management/delete_resource.html'

    def get(self, *a, **kw):
        if self.request.is_ajax():
            return super(ResourceDeleteView, self).get(*a, **kw)
        return redirect('dashboard:resources_management:resources_index')

    def get_success_url(self):
        return reverse_lazy('dashboard:resources_management:resources_index')

class ResourceDetailView(DetailView):
    context_object_name = 'recurso'
    model = Recurso
    queryset = Recurso.objects.all()
    template_name = 'dashboard/resources_management/detail_resource.html'
    http_method_names = ['get']

class ResourceUpdateView(UpdateView):
    form_class = ResourceForm
    model = Recurso
    queryset = Recurso.objects.all()
    template_name = 'dashboard/resources_management/update_resource.html'
    success_url = reverse_lazy('dashboard:resources_management:resources_index')

