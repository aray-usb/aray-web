from django.urls import path, re_path
from . import views

app_name = "accounts"

urlpatterns = [
    path(
        '', 
        views.auth, 
        name="auth"
    ),
    re_path(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'
    ),
    path(
        'cerrar-sesion/', 
        views.logout_view, 
        name="logout"
    ),
]
