from django import forms
from apps.api.models import Tarea


class TareaForm(forms.ModelForm):
    fecha_limite = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    class Meta:
        model = Tarea
        fields = '__all__'