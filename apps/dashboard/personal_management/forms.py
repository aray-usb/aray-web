
from django import forms
from apps.api.models import Organizacion, Voluntario


class OrganizacionCreateForm(forms.ModelForm):

    class Meta:
        model = Organizacion
        fields = '__all__'

class OrganizacionUpdateForm(forms.ModelForm):

    class Meta:
        model = Organizacion
        fields = '__all__'

class VoluntarioCreateForm(forms.ModelForm):

    class Meta:
        model = Voluntario
        fields = '__all__'

class VoluntarioUpdateForm(forms.ModelForm):

    class Meta:
        model = Voluntario
        fields = '__all__'