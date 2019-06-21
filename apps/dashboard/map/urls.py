"""
URLs (routing) para el mapa de incidencias del dashboard
"""

from django.urls import path
from . import views

app_name = "map"

urlpatterns = [
    path('incidencia/create/', views.IncidenciaCreateView.as_view(), name="incidence_create"),
    path('incidencia/update/<int:pk>/', views.IncidenciaUpdateView.as_view(), name="incidence_update"),
    path('reporte/update/<int:pk>/', views.ReporteUpdateView.as_view(), name="report_update"),
    path('incidencia/<int:pk>', views.IncidenciaDetailView.as_view(), name="incidence_detail"),
    path('', views.MapView.as_view(), name="incidence_map"),
]
