from django.shortcuts import render
from django.views import generic


class ResourcesView(generic.TemplateView):
    template_name = "dashboard/resources_management/resources_management.html"