from django.conf.urls import include
from django.urls import path
from .views import *

app_name = "resources_management"

urlpatterns = [
    path(
        '',
        ResourcesIndexView.as_view(),
        name='resources_index',
    ),
    path(
        'crear_recurso/',
        ResourceCreateView.as_view(),
        name='create_resource',
    ),
    path(
        'borrar_recurso/<int:pk>/',
        ResourceDeleteView.as_view(),
        name='delete_resource',
    ),
    path(
        'recurso/<int:pk>/',
        ResourceDetailView.as_view(),
        name='detail_resource',
    ),
    path(
        'actualizar_recurso/<int:pk>/',
        ResourceUpdateView.as_view(),
        name='update_resource',
    ),

]

