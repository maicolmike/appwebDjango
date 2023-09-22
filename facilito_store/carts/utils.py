from .models import Cart
def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id') #none
    cart = Cart.objects.filter(cart_id=cart_id).first() #None
    
    if cart is None:
        cart = Cart.objects.create(user=user)
    
    #asignarle usuario al carrito si nose habia logeado   
    if user and cart.user is None:
        cart.user = user
        cart.save()
    
    request.session['cart_id']= cart.cart_id #actualizar la sesion
    
    return cart

def destroy_cart(request):
    request.session['cart_id'] = None