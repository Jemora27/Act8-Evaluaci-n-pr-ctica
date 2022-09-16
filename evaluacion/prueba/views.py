from contextlib import redirect_stdout
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


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

def contacto(request):
    if request.method == "POST":
        email = request.POST['email']
        user = request.POST['user']
        message = request.POST['message']
        context = {
            'email': email,
            'user': user,
            'message': message
        }
        template = get_template('email_template.html')
        content = template.render(context)

        email = EmailMultiAlternatives(
            'FIFA WORLD CUP QATAR 2022',
            'FIFA WORLD CUP QATAR 2022',
            settings.EMAIL_HOST_USER,
            ['jo74ra@gmail.com']
        )

        email.attach_alternative(content, 'text/html')
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'contacto.html',{

    })
	 
