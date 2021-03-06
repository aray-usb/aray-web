"""
Controladores (views) referentes al manejo de sesiones de usuario.
"""

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .tokens import account_activation_token

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def register_process(request):

    form = UserCreationForm(data=request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        # user.is_active = False
        user.save()
        """
        current_site = get_current_site(request)
        message = render_to_string('accounts/activation.html', {
            'user':user,
            'domain':current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = '¡Activa tu cuenta en Aray!'
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')
        """
    else:
        messages.error(request, 'Credenciales introducidas incorrectas, intente de nuevo.')
        

    return render(request, 'accounts/auth.html', {'form': form})


def login_process(request):

    form = AuthenticationForm(data=request.POST)
    next_url = request.GET.get('next', 'dashboard:index')
    if form.is_valid():
        # Autenticamos al usuario en la sesión
        usuario = form.get_user()
        login(request, usuario)

        return redirect(next_url)
    else:
        messages.error(request, 'Credenciales introducidas incorrectas, intente de nuevo.')

def auth(request):
    """
    Controlador del formulario de registro e inicio de sesión.

    GET: Muestra la vista de login y registro.
    POST: Intenta realizar un registro o login, de acuerdo a sea el caso.
    """

    template_name="accounts/auth.html"

    # Redirigimos a usuarios ya autenticados
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    # Si la petición es POST, realizamos el proceso correspondiente
    if request.method == 'POST':
        if 'register' in request.POST:
            return register_process(request)
        elif 'login' in request.POST:
            login_attempt = login_process(request)
            if login_attempt:
                return login_attempt

    return render(request, template_name)

@login_required
def logout_view(request):
    """
    Cierra la sesión de un usuario logueado y redirige a la vista
    de inicio de sesión.
    """

    logout(request)
    return redirect('accounts:auth')
