"""
Implementación de distintos serializadores para enviar
información de los modelos de la aplicación a través de la API.
"""

from django.contrib.auth.models import User
from apps.api.models import (
    Incidencia,
    Reporte,
    Tarea,
    Voluntario
)
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador del modelo Usuario.
    """

    class Meta:
        """
        Clase interna para configurar detalles del serializador.
        """

        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
        )

class VoluntarioSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador del modelo Voluntario.
    """

    usuario = UsuarioSerializer()

    class Meta:
        """
        Clase interna para configurar detalles del serializador.
        """

        model = Voluntario
        fields = (
            'id',
            'usuario',
            'tipo_identidad',
            'nro_identidad',
        )

class IncidenciaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador del modelo Incidencia.
    """

    class Meta:
        """
        Clase interna para configurar detalles del serializador.
        """

        model = Incidencia
        fields = (
            'id',
            'latitud',
            'longitud',
            'radio',
            'nombre',
            'descripcion',
            'estado',
            'fecha_de_reporte',
            'fecha_de_resolucion',
        )

class ReporteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador del modelo Reporte.
    """

    incidencia = IncidenciaSerializer()
    reportado_por = VoluntarioSerializer()

    class Meta:
        """
        Clase interna para configurar detalles del serializador.
        """

        model = Reporte
        fields = (
            'id',
            'incidencia',
            'contenido',
            'estado',
            'latitud',
            'longitud',
            'fecha_de_reporte',
            'reportado_por',
            'es_solicitud_de_ayuda',
        )

class TareaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador del modelo Tarea.
    """

    class Meta:
        """
        Clase interna para configurar detalles del serializador.
        """

        model = Tarea
        fields = (
            'id',
            'titulo',
            'descripcion',
            'fecha_limite',
            'fecha_de_resolucion',
            'estado',
            'asignada_por',
            'asignada_a',
        )
