"""
URLs (routing) para el manejo de sesiones, inicio y cierre de sesión,
registro, entre otras opciones.
"""

from django.urls import path
from . import views

app_name = "sesiones"

urlpatterns = [
    path('', views.login_view, name="login"),
    path('cerrar-sesion/', views.logout_view, name="logout"),
]
