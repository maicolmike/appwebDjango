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