"""
Implementación de los distintos endpoints de la API
a través de views y viewsets.
"""

from rest_framework import mixins, viewsets

from apps.api.models import Incidencia, Reporte, Tarea
from apps.api.serializers import IncidenciaSerializer, ReporteSerializer, TareaSerializer

class IncidenciaViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Endpoint de la API para listar, actualizar y
    ver detalles de las incidencias.

    Métodos permitidos: GET, PUT, PATCH.
    """

    queryset = Incidencia.objects.all().order_by('-fecha_de_reporte')
    serializer_class = IncidenciaSerializer

class ReporteViewSet(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    Endpoint de la API para listar, actualizar y
    ver detalles de los reportes.

    Métodos permitidos: GET, POST, PUT, PATCH.
    """

    queryset = Reporte.objects.all().order_by('-fecha_de_reporte')
    serializer_class = ReporteSerializer

class TareaViewSet(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    Endpoint de la API para listar, actualizar y
    ver detalles de las tareas.

    Métodos permitidos: GET, PUT, PATCH.
    """

    queryset = Tarea.objects.all().order_by('fecha_limite')
    serializer_class = TareaSerializer