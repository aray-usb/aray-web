"""
Patrones de URLs para los endpoints de la API.
"""

from django.urls import include, path
from rest_framework import routers
from api import views

# Instancia un enrutador para manejas las URLs de la API
router = routers.DefaultRouter()
router.register(
    r'incidencias',
    views.IncidenciaViewSet
)

app_name = "api"

urlpatterns = [
    path('', include(router.urls)),
]
