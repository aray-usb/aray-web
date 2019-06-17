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
from apps.api.models import Tarea
from .forms import *



class IndexView(TemplateView):
    template_name = "dashboard/assignments/assignments.html"
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] =  Tarea.objects.all()
        return context

class TareaCreateView(CreateView):
    form_class = TareaForm
    model = Tarea
    queryset = Tarea.objects.all()
    template_name = 'dashboard/assignments/create_assignment.html'
    success_url = reverse_lazy('dashboard:personal_management:assignments')

class TareaDeleteView(DeleteView):
    context_object_name = 'tarea'
    model = Tarea
    template_name = 'dashboard/personal_management/delete_assignment.html'
    success_url = reverse_lazy('dashboard:personal_management:assignments')

class TareaDetailView(DetailView):
    context_object_name = 'tarea'
    model = Tarea
    queryset = Tarea.objects.all()
    template_name = 'dashboard/personal_management/detail_assignment.html'
    http_method_names = ['get']

class TareaUpdateView(UpdateView):
    form_class = TareaForm
    model = Tarea
    queryset = Tarea.objects.all()
    template_name = 'dashboard/assignments/update_assignment.html'
    success_url = reverse_lazy('dashboard:assignments:assignments')


