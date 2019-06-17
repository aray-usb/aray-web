from django import forms
from apps.api.models import Tarea


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'