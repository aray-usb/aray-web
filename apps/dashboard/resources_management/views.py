from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Resource
from .forms import ResourceForm


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class ResourcesView(generic.TemplateView):
    template_name = "dashboard/resources_management/resources_management.html"

class AddResource(AjaxableResponseMixin, CreateView):

    model = Resource
    template_name = 'dashboard/resources_management/resources-form.html'
    form_class = ResourceForm

    def get_initial(self):
        initial = super(AddResource, self).get_initial()
        return initial