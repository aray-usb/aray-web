"""
URLs (routing) para el gestor de personal del dashboard
"""

from django.urls import path
from . import views

app_name = "personal_management"

urlpatterns = [
    path('', views.PersonalView.as_view(), name="personal"),
]
