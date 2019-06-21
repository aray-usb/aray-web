from apps.api.models import Incidencia
from django import template

register = template.Library()

@register.filter(name='incidencias_en_curso')
def incidencias_en_curso(val):
    return Incidencia.objects.exclude(
        estado=Incidencia.ESTADO_RECHAZADA
    ).exclude(
        estado=Incidencia.ESTADO_RESUELTA
    )

@register.filter(name='cantidad_incidencias_en_curso')
def cantidad_incidencias_en_curso(val):
    return incidencias_en_curso(val).count()