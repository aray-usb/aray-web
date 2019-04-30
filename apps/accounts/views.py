from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse_lazy

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from django.template.loader import render_to_string


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
        user.is_active = False
        user.save()
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
    else:
        print(form.errors)
        print('yujuuu')

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
        print('no lo logramos :(')
        #messages.error(request, 'Document deleted.')

def auth(request):
    
    template_name="accounts/auth.html"
    # Redirigimos a usuarios ya autenticados
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    
    if 'register' in request.POST and request.method == 'POST':
        register_process(request)
    elif 'login' in request.POST and request.method == 'POST':
        login_process(request)

    return render(request, template_name)

@login_required
def logout_view(request):
    """
    Cierra la sesión de un usuario logueado y redirige a la vista
    de inicio de sesión.
    """

    logout(request)
    return redirect('accounts:auth')

