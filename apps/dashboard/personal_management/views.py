from django.shortcuts import render
from django.views import generic

class PersonalView(generic.TemplateView):
    template_name = "dashboard/personal_management/personal_management.html"
