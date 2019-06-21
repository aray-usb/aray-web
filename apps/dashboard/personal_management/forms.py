
from django import forms
from apps.api.models import Organizacion, Voluntario


class OrganizacionForm(forms.ModelForm):
    dirigida_por = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Voluntario.objects.all())
    class Meta:
        model = Organizacion
        fields = '__all__'

class VoluntarioForm(forms.ModelForm):

    class Meta:
        model = Voluntario
        fields = '__all__'

