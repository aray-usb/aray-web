
from django.conf.urls import include
from django.urls import path
from .views import *


app_name = "assignments"

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='assignments_index',
    ),
    path(
        'crear_tarea/',
        TareaCreateView.as_view(),
        name='create_assignment',
    ),
    path(
        'borrar_tarea/<int:pk>/',
        TareaDeleteView.as_view(),
        name='delete_assignment',
    ),
    path(
        'tarea/<int:pk>/',
        TareaDetailView.as_view(),
        name='detail_assignment',
    ),
    path(
        'actualizar_tarea/<int:pk>/',
        TareaUpdateView.as_view(),
        name='update_assignment',
    ),

]
