"""
Implementación de los distintos endpoints de la API
a través de views y viewsets.
"""

from apps.api.models import (
    Incidencia,
    Reporte
)
from apps.api.serializers import (
    IncidenciaSerializer,
    ReporteSerializer
)

from rest_framework import viewsets, mixins

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
