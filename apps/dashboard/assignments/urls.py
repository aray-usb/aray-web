"""
URLs (routing) para el gestor de tareas de la aplicación
"""

from django.urls import path, include
from . import views

app_name = "assignments"

urlpatterns = [
    path('', views.AssignmentsView.as_view(), name="assignments"),
]