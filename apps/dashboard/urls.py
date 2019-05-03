"""
URLs (routing) para el dashboard de la aplicación
"""

from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.DashboardView.as_view(), name="index"),
    path('resources', include('apps.dashboard.resources_management.urls')),
]
