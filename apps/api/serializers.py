"""
Implementación de distintos serializadores para enviar
información de los modelos de la aplicación a través de la API.
"""

from apps.api.models import Incidencia
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
