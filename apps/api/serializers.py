"""
Implementación de distintos serializadores para enviar
información de los modelos de la aplicación a través de la API.
"""

from apps.api.models import (
    Incidencia,
    Reporte,
    Tarea
)
from rest_framework import serializers

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
            'fecha_de_reporte',
            'reportado_por'
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
