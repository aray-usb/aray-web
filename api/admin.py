from django.contrib import admin
from api.models import (
    Voluntario,
    Tarea,
    Incidencia,
    Reporte,
    Organizacion,
    Recurso,
    RecursoAsignado
)

# Registra los modelos de la base de datos en el admin de Django
admin.site.register(Voluntario)
admin.site.register(Tarea)
admin.site.register(Incidencia)
admin.site.register(Reporte)
admin.site.register(Organizacion)
admin.site.register(Recurso)
admin.site.register(RecursoAsignado)