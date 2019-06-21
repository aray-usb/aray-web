"""
Implementación de los distintos endpoints de la API
a través de views y viewsets.
"""

import decimal

from django.contrib.auth.models import User

from rest_framework import mixins, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.api.models import (
    Incidencia,
    Reporte,
    Tarea,
    Voluntario,
)

from apps.api.serializers import (
    IncidenciaSerializer,
    ReporteSerializer,
    TareaSerializer
)

class EstadoTareaView(APIView):
    """
    Endpoint personalizado para cambiar el estado de una tarea
    desde la app.
    """

    def post(self, request, format=None):
        """
        Intenta cambiar el estado de una tarea y devolver
        el resultado.
        """

        try:
            id_tarea = int(request.data['id'])
            nuevo_estado = int(request.data['estado'])
        except KeyError:
            return Response({"success": False, "content": "No se proporcionaron todos los datos."}, status=400)
        except ValueError:
            return Response({"success": False, "content": "Los datos proporcionados son inválidos."}, status=400)

        try:
            tarea = Tarea.objects.get(pk=id_tarea)
        except Tarea.DoesNotExist:
            return Response({"success": False, "content": "ID de Tarea incorrecto."}, status=400)

        tarea.estado = nuevo_estado
        tarea.save()

        return Response({"success": True, "content": "Tarea actualizada con éxito."}, status=201)

class RegistroView(APIView):
  """
  Endpoint personalizado para el registro desde la app.
  """

  authentication_classes = ([])
  permission_classes = ([])

  def post(self, request, format=None):
    """
    Intenta registrar un usuario y devolver su información.
    """

    try:
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        phone = request.data['phone']
        document = request.data['document']
    except KeyError:
        return Response({"success": False, "content": "No se proporcionaron todos los datos."}, status=400)

    usuario_existente = User.objects.filter(email=email) | User.objects.filter(username=username)
    voluntario_existente = Voluntario.objects.filter(nro_identidad=document)

    if usuario_existente.count() > 0 or voluntario_existente.count() > 0:
        return Response({"success": False, "content": "Ya existe un usuario con tus datos"}, status=400)

    usuario = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_active=True
    )
    usuario.set_password(password)
    usuario.save()

    telefono = "({0}) {1}-{2}".format(
        str(phone)[0:4],
        str(phone)[4:7],
        str(phone)[7:11],
    )

    voluntario = Voluntario(
        usuario=usuario,
        telefono=telefono,
        nro_identidad=int(document)
    )
    voluntario.save()

    return Response({"success": True, "content": "Usuario creado con éxito."}, status=201)

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
                descripcion="Pendiente de revision",
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

    def create(self, request, *args, **kwargs):
        """
        Crea una nueva tarea asignada al usuario.
        """

        try:
            voluntario = request.user.voluntario
        except:
            voluntario = None


        tarea = Tarea(
            titulo=request.data['titulo'],
            descripcion=request.data['descripcion'],
            fecha_limite=request.data['fecha_limite'],
            asignada_a=voluntario,
            asignada_por=voluntario
        )
        tarea.save()

        serializer = self.get_serializer(tarea)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
