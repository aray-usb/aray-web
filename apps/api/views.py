"""
Implementación de los distintos endpoints de la API
a través de views y viewsets.
"""

import decimal

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from apps.api.models import (
    Incidencia,
    Reporte,
    Tarea
)

from apps.api.serializers import (
    IncidenciaSerializer,
    ReporteSerializer,
    TareaSerializer
)

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

    def list(self, request, *args, **kwargs):
        """
        Retorna una respuesta que enlista los reportes.
        Ubica los reportes a menos de 5km de una latitud y longitud, si se pasa.
        """

        # Intentamos obtener parámetros de ubicación para filtrar
        latitud = float(request.GET.get('lat'))
        longitud = float(request.GET.get('long'))

        if latitud is not None and longitud is not None:
            queryset = Reporte.obtener_cercanos(latitud, longitud)
        else:
            queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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