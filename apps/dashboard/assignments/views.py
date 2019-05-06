from django.shortcuts import render
from django.views import generic

class AssignmentsView(generic.TemplateView):
    template_name = "dashboard/assignments/assignments_list.html"