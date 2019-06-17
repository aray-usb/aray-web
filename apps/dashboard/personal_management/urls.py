
from django.conf.urls import include
from django.urls import path
from .views import *

app_name = "personal_management"

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='personal_index',
    ),
    path(
        'crear_organizacion/',
        OrganizacionCreateView.as_view(),
        name='create_organization',
    ),
    path(
        'borrar_organizacion/<int:pk>/',
        OrganizacionDeleteView.as_view(),
        name='delete_organization',
    ),
    path(
        'organizacion/<int:pk>/',
        OrganizacionDetailView.as_view(),
        name='detail_organization',
    ),
    path(
        'actualizar_organizacion/<int:pk>/',
        OrganizacionUpdateView.as_view(),
        name='update_organization',
    ),

]
