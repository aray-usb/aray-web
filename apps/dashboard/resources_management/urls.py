from django.conf.urls import include
from django.urls import path
from .views import ResourcesIndexView, ResourcesCreateView

app_name = "resources_management"

urlpatterns = [
    path(
        '',
        ResourcesIndexView.as_view(),
        name='resources_index',
    ),
    path(
        'crear_recurso/',
        ResourcesCreateView.as_view(),
        name='create_resource',
    ),

]

