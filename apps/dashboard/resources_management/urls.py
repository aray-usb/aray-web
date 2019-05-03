"""
URLs (routing) para el gestor de recursos del dashboard
"""

from django.urls import path
from . import views

app_name = "resources_management"

urlpatterns = [
    path('', views.ResourcesView.as_view(), name="resources"),
    path('anadir/', views.AddResource.as_view(), name='add'),
]
