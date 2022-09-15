from contextlib import redirect_stdout
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


#Index

def index(request):
    return render (request, 'index.html', {
        
    })

def interface(request):
    return render (request, 'interface.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('interface')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada con exito.')
    return redirect('index')
