from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hola mundo") # funciona con rom django.http import HttpResponse
    return render(request, 'index.html',{
        'mensaje':"Listado de productos",
        'title': "Index dinamico",
        'products':[{'title':'playera', 'price':5, 'stock':True},
                    {'title':'camiseta', 'price':4, 'stock':False},
                    ]
    })