from django.shortcuts import render

# Create your views here.
from .models import Cart
from .utils import get_or_create_cart

def cart (request):
    cart = get_or_create_cart(request)
    
    return render(request,'carts/cart.html',{
    })
    
    #crear la session
    ##request.session['cart_id'] = '123'
    
    #obtenet la informacion
    #valor = request.session.get('cart_id')
    #print (valor)
    
    #eliminar una sesion 
    #request.session['cart_id'] = None
    
    #request.session['cart_id']= None
    # obtener usuario autenticado y validar