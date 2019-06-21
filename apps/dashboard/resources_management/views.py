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

        context["recursos"] = Recurso.objects.all()
        context["articulos"] = context["recursos"].count()
        
        # Porcentajes de Recursos
        try:
            context["articulos_medicina"] = str(
                (
                    Recurso.objects.filter(tipo=Recurso.TIPO_MEDICINAS).count() / context["articulos"]
                ) * 100
            )
        except ZeroDivisionError:
            context["articulos_medicina"] = 0

        try:
            context["articulos_alimentacion"] = str(
                (
                    Recurso.objects.filter(tipo=Recurso.TIPO_ALIMENTACION).count() / context["articulos"]
                ) * 100
            )
        except ZeroDivisionError:
            context["articulos_alimentacion"] = 0

        try:
            context["articulos_rescate"] = str(
                (
                    Recurso.objects.filter(tipo=Recurso.TIPO_ARTICULO_RESCATE).count() / context["articulos"]
                ) * 100
            )
        except ZeroDivisionError:
            context["articulos_rescate"] = 0
        
        try:
            context["articulos_transporte"] = str(
                (
                    Recurso.objects.filter(tipo=Recurso.TIPO_TRANSPORTE).count() / context["articulos"]
                ) * 100
            )
        except ZeroDivisionError:
            context["articulos_transporte"] = 0

        try:
            context["articulos_otros"] = str(
                (
                    Recurso.objects.filter(tipo=Recurso.TIPO_OTROS).count() / context["articulos"]
                ) * 100
            )
        except ZeroDivisionError:
            context["articulos_otros"] = 0
        
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

