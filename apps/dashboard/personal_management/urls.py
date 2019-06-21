
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


    path(
        'crear_voluntario/',
        VoluntarioCreateView.as_view(),
        name='create_v',
    ),
    path(
        'borrar_voluntario/<int:pk>/',
        VoluntarioDeleteView.as_view(),
        name='delete_v',
    ),
    path(
        'voluntario/<int:pk>/',
        VoluntarioDetailView.as_view(),
        name='detail_v',
    ),
    path(
        'actualizar_voluntario/<int:pk>/',
        VoluntarioUpdateView.as_view(),
        name='update_v',
    ),

]
