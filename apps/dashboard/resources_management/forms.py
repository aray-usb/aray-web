from django import forms
from .models import Resource


class ResourceForm(forms.ModelForm):

    class Resources:
        model = Resource 
        fields = ['name', 'resource_type', 'register_date', 'purchase_prize', 'items_cuantity']
