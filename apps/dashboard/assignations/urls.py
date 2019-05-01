
from django.urls import path, include
from . import views

app_name = "assignations"

urlpatterns = [
    path('', views.AssignationsView.as_view(), name="assignations"),
]