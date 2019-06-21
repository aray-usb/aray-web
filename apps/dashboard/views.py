from django.shortcuts import render
from django.views import generic

from apps.api.models import (
    Organizacion,
    Reporte,
    Tarea,
    Incidencia,
    Recurso,
    Voluntario,
)

"""
Vistas para el Dashboard de Aray
"""

class DashboardView(generic.TemplateView):
    """
    Despliega el Dashboard inicial al usuario.
    """

    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["organizaciones"] = Organizacion.objects.count()
        context["voluntarios"] = Voluntario.objects.count()
        context["incidencias"] = Incidencia.objects.count()
        context["reportes"] = Reporte.objects.count()
        context["asignaciones"] = Tarea.objects.count()
        context["articulos"] = Recurso.objects.count()

        # Porcentajes de Tareas
        try:
            context["tareas_nuevas"] = str(
                (
                    Tarea.objects.filter(estado=Tarea.ESTADO_NUEVA).count() / context["asignaciones"]
                ) * 100
            )
        except ZeroDivisionError:
            context["tareas_nuevas"] = 0

        try:
            context["tareas_en_progreso"] = str(
                (
                    Tarea.objects.filter(estado=Tarea.ESTADO_EN_PROGRESO).count() / context["asignaciones"]
                ) * 100
            )
        except ZeroDivisionError:
            context["tareas_en_progreso"] = 0

        try:
            context["tareas_realizadas"] = str(
                (
                    Tarea.objects.filter(estado=Tarea.ESTADO_RESUELTA).count() / context["asignaciones"]
                ) * 100
            )
        except ZeroDivisionError:
            context["tareas_realizadas"] = 0
        
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

        return context
