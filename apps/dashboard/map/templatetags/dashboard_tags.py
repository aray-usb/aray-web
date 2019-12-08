from apps.api.models import Incidencia
from django import template

register = template.Library()

@register.filter()
def incidencias_en_curso(val):
    return Incidencia.objects.exclude(
        estado=Incidencia.ESTADO_RECHAZADA
    ).exclude(
        estado=Incidencia.ESTADO_RESUELTA
    )

@register.filter()
def cantidad_incidencias_en_curso(val):
    return incidencias_en_curso(val).count()

@register.filter()
def hay_incidencias_en_curso(val):
    return incidencias_en_curso().exists()