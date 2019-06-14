
from django import forms
from apps.api.models import Organizacion, Voluntario


class OrganizacionCreateForm(forms.ModelForm):

    class Meta:
        model = Organizacion
        fields = (
            'nombre',
            'latitud',
            'longitud',
            'dirigida_por',
        )

class OrganizacionUpdateForm(forms.ModelForm):

    class Meta:
        model = Organizacion
        fields = (
            'nombre',
            'latitud',
            'longitud',
            'dirigida_por',
        )

class VoluntarioCreateForm(forms.ModelForm):

    class Meta:
        model = Voluntario
        fields = '__all__'

class VoluntarioUpdateForm(forms.ModelForm):

    class Meta:
        model = Voluntario
        fields = '__all__'