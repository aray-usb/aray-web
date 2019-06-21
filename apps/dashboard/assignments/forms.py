from django import forms
from apps.api.models import Tarea


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = (
            'titulo',
            'descripcion',
            'fecha_limite',
            'fecha_de_resolucion',
            'estado',
            'asignada_a',
        )