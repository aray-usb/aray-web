"""
URLs (routing) para el dashboard de la aplicación
"""

from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.DashboardView.as_view(), name="index"),
]
