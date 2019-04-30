"""
URLs (routing) para el dashboard de la aplicación
"""

from django.urls import path
from . import views
from apps.dashboard.resources_management.views import ResourcesView

app_name = "dashboard"

urlpatterns = [
    path('', views.DashboardView.as_view(), name="index"),
    path('resources', ResourcesView.as_view(), name="resources_management"),
]
