"""
Implementación de los distintos endpoints de la API
a través de views y viewsets.
"""

import decimal

from rest_framework import mixins, status, viewsets
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
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Endpoint de la API para listar, actualizar y
    ver detalles de las incidencias.

    Métodos permitidos: GET.
    """

    queryset = Incidencia.objects.all().order_by('-fecha_de_reporte')
    serializer_class = IncidenciaSerializer

class ReporteViewSet(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    Endpoint de la API para listar, actualizar y
    ver detalles de los reportes.

    Métodos permitidos: GET, POST, PUT, PATCH.
    """

    queryset = Reporte.objects.all().order_by('-fecha_de_reporte')
    serializer_class = ReporteSerializer

    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo reporte, creando una incidencia nueva en caso
        de ser necesario.
        """

        incidencia_id = int(request.data.get('incidencia', -1))

        if incidencia_id is None or incidencia_id == -1:
            incidencia = Incidencia(
                nombre="Nueva incidencia por confirmar",
                descripcion="Pendiente de revisión",
                latitud=decimal.Decimal(request.data['latitud']),
                longitud=decimal.Decimal(request.data['longitud']),
            )
            incidencia.save()
        else:
            incidencia = Incidencia.objects.get(
                pk=incidencia_id
            )

        try:
            voluntario = request.user.voluntario
        except:
            voluntario = None

        if request.data['es_solicitud_de_ayuda'] == "true":
            esAyuda = True
        else:
            esAyuda = False

        reporte = Reporte(
            latitud=decimal.Decimal(request.data['latitud']),
            longitud=decimal.Decimal(request.data['longitud']),
            incidencia=incidencia,
            contenido=request.data['contenido'],
            reportado_por=voluntario,
            es_solicitud_de_ayuda=esAyuda
        )
        reporte.save()

        serializer = self.get_serializer(reporte)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
            q = self.get_queryset().exclude(
                incidencia__estado=Incidencia.ESTADO_RECHAZADA
            ).exclude(
                incidencia__estado=Incidencia.ESTADO_RESUELTA
            )
            queryset = self.filter_queryset(q)

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

    def list(self, request, *args, **kwargs):
        """
        Retorna una respuesta que enlista las tareas.
        Incluye solo las tareas del usuario en cuestión.
        """

        try:
            q = self.get_queryset().filter(
                asignada_a=request.user.voluntario
            )
            queryset = self.filter_queryset(q)
        except:
            queryset = Tarea.objects.none()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
