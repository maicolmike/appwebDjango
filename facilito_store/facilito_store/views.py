from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages

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
        
    })