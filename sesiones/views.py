from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import generic

"""
Vistas para el manejo de Sesiones de Aray
"""

def login_view(request):
    """
    Muestra el formulario de inicio de sesión si se recibe una petición GET.
    En caso de recibir una petición POST, intenta validar los datos introducidos
    para autenticar un posible usuario, o retorna la vista con los datos instanciados
    mostrando el error correspondiente.
    """

    template_name="sesiones/login.html"

    # Redirigimos a usuarios ya autenticados
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        # Se obtienen los datos recibidos por POST y se intenta autenticar
        # al usuario

        form = AuthenticationForm(data=request.POST)
        next_url = request.GET.get('next', 'dashboard:index')
        print(request.POST)
        if form.is_valid():
            # Autenticamos al usuario en la sesión
            usuario = form.get_user()
            login(request, usuario)

            return redirect(next_url)
    else:
        # Si los datos son incorrectos, se muestra el formulario
        # y un mensaje de error
        messages.error(request, "Los datos introducidos no son correctos.")
    return render(request, template_name)

@login_required
def logout_view(request):
    """
    Cierra la sesión de un usuario logueado y redirige a la vista
    de inicio de sesión.
    """

    logout(request)
    return redirect('sesiones:login')
