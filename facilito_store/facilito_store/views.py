from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
#from django.contrib.auth.models import User
from users.models import User
from products.models import Product
from django.http import HttpResponseRedirect

def index(request):
    # return HttpResponse("Hola mundo") # funciona con rom django.http import HttpResponse
    products = Product.objects.all().order_by('id')
    
    return render(request, 'index.html',{
        'mensaje':"Listado de productos",
        'title': "Index dinamico",
        'products': products,
    })
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
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
    if request.user.is_authenticated:
        return redirect('index')
    
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