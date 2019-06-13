from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
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


class OrganizacionCreateView(CreateView):
    form_class = OrganizacionCreateForm
    model = Organizacion
    queryset = Organizacion.objects.all()
    template_name = 'dashboard/personal_management/create_organization.html'
    success_url = reverse_lazy('dashboard:personal_management:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['base_url'] = 'http://%s' % get_current_site(self.request).domain
        return ctx

class OrganizacionDeleteView(DeleteView):
    context_object_name = 'organizacion'
    model = Organizacion
    success_url = reverse_lazy('dashboard:personal_management:index')

class OrganizacionDetailView(DetailView):
    context_object_name = 'organizacion'
    model = Organizacion
    queryset = Organizacion.objects.all()
    template_name = 'dashboard/personal_management/detail_organization.html'
    http_method_names = ['get']


class OrganizacionUpdateView(UpdateView):
    form_class = OrganizacionUpdateForm
    model = Organizacion
    queryset = Organizacion.objects.all()
    template_name = 'dashboard/personal_management/update_organization.html'
    success_url = reverse_lazy('dashboard:personal_management:index')


class OrganizacionListView(JQueryDataTablesMixin, ListView):
    
    http_method_names = ['post']
    model = Organizacion
    search_attributes = ["id", "nombre"]

    def serialize_page(self, page, **kwargs):
        table_list = []

        for idx, organization in enumerate(page):
            tablerow = dict()
            tablerow['number'] = idx + kwargs['start'] + 1
            tablerow['id'] = organization.id
            tablerow['company_name'] = client.nombre
            
            table_list.append(tablerow)

        return table_list

