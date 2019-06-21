"""
Patrones de URLs para los endpoints de la API.
"""

from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)
from apps.api import views

# Instancia un enrutador para manejas las URLs de la API
router = routers.DefaultRouter()
router.register(
    r'incidencias',
    views.IncidenciaViewSet
)
router.register(
    r'reportes',
    views.ReporteViewSet
)
router.register(
    r'tareas',
    views.TareaViewSet
)

app_name = "api"

urlpatterns = [
    path('', include(router.urls)),
    path('tokens/get/', obtain_jwt_token),
    path('tokens/refresh/', refresh_jwt_token),
    path('tokens/verify/', verify_jwt_token),
    path('registro/', views.RegistroView.as_view()),
    path('actualizar-tarea/', views.EstadoTareaView.as_view()),
]
