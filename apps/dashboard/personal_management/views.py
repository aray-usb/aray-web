from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
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
from apps.api.models import Organizacion, Voluntario
from .forms import *



class IndexView(TemplateView):
    template_name = "dashboard/personal_management/personal_management.html"
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["organizaciones"] =  Organizacion.objects.all()
        context["voluntarios"] = Voluntario.objects.all()
        return context

class OrganizacionCreateView(CreateView):
    form_class = OrganizacionForm
    model = Organizacion
    queryset = Organizacion.objects.all()
    template_name = 'dashboard/personal_management/create_organization.html'
    success_url = reverse_lazy('dashboard:personal_management:personal_index')

class OrganizacionDeleteView(DeleteView):
    context_object_name = 'organizacion'
    model = Organizacion
    template_name = 'dashboard/personal_management/delete_organization.html'

    def get(self, *a, **kw):
        if self.request.is_ajax():
            return super(OrganizacionDeleteView, self).get(*a, **kw)
        return redirect('dashboard:personal_management:personal_index')

    def get_success_url(self):
        return reverse_lazy('dashboard:personal_management:personal_index')

class OrganizacionDetailView(DetailView):
    context_object_name = 'organizacion'
    model = Organizacion
    queryset = Organizacion.objects.all()
    template_name = 'dashboard/personal_management/detail_organization.html'
    http_method_names = ['get']

class OrganizacionUpdateView(UpdateView):
    form_class = OrganizacionForm
    model = Organizacion
    queryset = Organizacion.objects.all()
    template_name = 'dashboard/personal_management/update_organization.html'
    success_url = reverse_lazy('dashboard:personal_management:personal_index')

class VoluntarioCreateView(CreateView):
    form_class = VoluntarioForm
    model = Voluntario
    queryset = Voluntario.objects.all()
    template_name = 'dashboard/personal_management/create_voluntario.html'
    success_url = reverse_lazy('dashboard:personal_management:personal_index')

class VoluntarioDeleteView(DeleteView):
    context_object_name = 'voluntario'
    model = Voluntario
    template_name = 'dashboard/personal_management/delete_voluntario.html'

    def get(self, *a, **kw):
        if self.request.is_ajax():
            return super(VoluntarioDeleteView, self).get(*a, **kw)
        return redirect('dashboard:personal_management:personal_index')

    def get_success_url(self):
        return reverse_lazy('dashboard:personal_management:personal_index')

class VoluntarioDetailView(DetailView):
    context_object_name = 'voluntario'
    model = Voluntario
    queryset = Voluntario.objects.all()
    template_name = 'dashboard/personal_management/detail_voluntario.html'
    http_method_names = ['get']

class VoluntarioUpdateView(UpdateView):
    form_class = VoluntarioForm
    model = Voluntario
    queryset = Voluntario.objects.all()
    template_name = 'dashboard/personal_management/update_voluntario.html'
    success_url = reverse_lazy('dashboard:personal_management:personal_index')


