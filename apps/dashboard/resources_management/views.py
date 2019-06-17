
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from utils.mixins.datatablesmixin import JQueryDataTablesMixin
from .forms import *
from apps.api.models import Recurso



class ResourcesIndexView(TemplateView):
    template_name = 'dashboard/resources_management/resources_management.html'
    http_method_names = ['get']


class ResourcesCreateView(CreateView):
    form_class = ResourceForm
    model = Recurso
    queryset = Recurso.objects.all()
    template_name = 'dashboard/resources_management/create_resource.html'
    success_url = reverse_lazy('dashboard:resources_management:resources')


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['base_url'] = 'http://%s' % get_current_site(self.request).domain
        return ctx

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return super().form_valid(form)


