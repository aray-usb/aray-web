from django import forms
from apps.api.models import Incidencia, Reporte

class IncidenciaForm(forms.ModelForm):

    class Meta:
        model = Incidencia
        fields = (
            'nombre',
            'descripcion',
            'latitud',
            'longitud',
            'radio',
            'estado',
        )

class ReporteForm(forms.ModelForm):

    class Meta:
        model = Reporte
        fields = (
            'incidencia',
            'contenido',
            'latitud',
            'longitud',
            'estado',
            'reportado_por',
        )