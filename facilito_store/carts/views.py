from django.shortcuts import render

# Create your views here.
from .models import Cart

def cart (request):
    #crear la session
    ##request.session['cart_id'] = '123'
    
    #obtenet la informacion
    #valor = request.session.get('cart_id')
    #print (valor)
    
    #eliminar una sesion 
    #request.session['cart_id'] = None
    
    # obtener usuario autenticado y validar
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        cart = Cart.objects.get(pk=cart_id) #obtenemos el carrito de la base de datos
    else:
        cart = Cart.objects.create(user=user) # generamos el carrito de compras
    
    request.session['cart_id']= cart.id #actualizar la sesion
    
    return render(request,'carts/cart.html',{
    })