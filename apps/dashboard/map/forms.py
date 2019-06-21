from django import forms
from apps.api.models import Incidencia

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