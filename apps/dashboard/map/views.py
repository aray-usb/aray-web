from django.shortcuts import render
from django.views import generic
from apps.api.models import Incidencia, Reporte
from .forms import IncidenciaForm, ReporteForm
from django.urls import reverse_lazy
from aray.settings import MAPBOX_API_KEY

class MapView(generic.TemplateView):
    """
    Controlador para la vista del mapa de incidencias
    """

    template_name = "dashboard/map/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["incidencias"] = Incidencia.objects.exclude(
            estado=Incidencia.ESTADO_RECHAZADA
        ).exclude(
            estado=Incidencia.ESTADO_RESUELTA
        )
        context["incidencias_tabla"] = Incidencia.objects.all()
        context["reportes"] = Reporte.objects.exclude(
            incidencia__estado=Incidencia.ESTADO_RECHAZADA
        ).exclude(
            incidencia__estado=Incidencia.ESTADO_RESUELTA
        )
        context['api_key'] = MAPBOX_API_KEY
        return context

class IncidenciaDetailView(generic.DetailView):
    context_object_name = 'incidencia'
    model = Incidencia
    queryset = Incidencia.objects.all()
    template_name = 'dashboard/map/detail_incidencia.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reportes"] = Reporte.objects.filter(incidencia=self.get_object())
        return context


class IncidenciaCreateView(generic.CreateView):
    form_class = IncidenciaForm
    model = Incidencia
    queryset = Incidencia.objects.all()
    template_name = 'dashboard/map/create_incidencia.html'
    success_url = reverse_lazy('dashboard:map:incidence_map')

class IncidenciaUpdateView(generic.UpdateView):
    form_class = IncidenciaForm
    model = Incidencia
    queryset = Incidencia.objects.all()
    template_name = 'dashboard/map/update_incidencia.html'
    success_url = reverse_lazy('dashboard:map:incidence_map')

class ReporteUpdateView(generic.UpdateView):
    form_class = ReporteForm
    model = Reporte
    queryset = Reporte.objects.all()
    template_name = 'dashboard/map/update_reporte.html'
    success_url = reverse_lazy('dashboard:map:incidence_map')