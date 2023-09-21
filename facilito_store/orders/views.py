from django.shortcuts import render

# Create your views here.
from carts.utils import get_or_create_cart
from .models import Order
from .utils import get_or_create_order
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb

@login_required(login_url='login')
def order (request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
        
    return render(request, 'orders/order.html', {
        'cart': cart,
        'order': order,
        'breadcrumb': breadcrumb()
    })
    
@login_required(login_url='login')
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    
    #shipping_address = order.shipping_address #forma de tener la dirrecion de nuestra orden
    shipping_address = order.get_or_set_shipping_address()
    return render(request, 'orders/address.html', {
        'cart': cart,
        'order': order,
        'shipping_address': shipping_address,
        'breadcrumb': breadcrumb(address=True)
    })