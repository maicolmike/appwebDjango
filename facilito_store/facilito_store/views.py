from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.models import User

def index(request):
    # return HttpResponse("Hola mundo") # funciona con rom django.http import HttpResponse
    return render(request, 'index.html',{
        'mensaje':"Listado de productos",
        'title': "Index dinamico",
        'products':[{'title':'playera', 'price':5, 'stock':True},
                    {'title':'camiseta', 'price':4, 'stock':False},
                    {'title':'pantaloneta', 'price':8, 'stock':True},
                    {'title':'zapatos', 'price':2, 'stock':False},
                    ]
    })
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else : 
            messages.error(request,'Usuario o contraseña incorrectos')
            
    return render(request, 'users/login.html',{
        'title': "Login",
        
    })
    
def logout_view(request):
    logout(request)
    messages.success(request,'Sesion cerrada')
    return redirect('login')

def register (request):
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        #username = form.cleaned_data.get('username')
        #email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')
        
        #user = User.objects.create_user(username, email, password)
        user = form.save() #save () se encuentra en el archivo forms.py
        if user:
            login(request, user) # se logee el usuario que creamos
            messages.success(request, 'usuario creado')
            return redirect('index')
            
    
    return render(request, 'users/register.html',{
        'form': form,
        'title': "Registro",
    })