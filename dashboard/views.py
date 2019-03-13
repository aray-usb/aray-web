from django.shortcuts import render
from django.views import generic

"""
Vistas para el Dashboard de Aray
"""

class DashboardView(generic.TemplateView):
    """
    Despliega el Dashboard inicial al usuario.
    """

    template_name = "dashboard/index.html"
