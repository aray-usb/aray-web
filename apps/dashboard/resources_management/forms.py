from django import forms
from apps.api.models import Recurso


class ResourceForm(forms.ModelForm):

    class Meta:
        model = Recurso 
        fields = '__all__'
