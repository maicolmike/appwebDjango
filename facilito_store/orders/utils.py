from .models import Order

def get_or_create_order (cart, request):
    
    order = Order.objects.filter(cart = cart).first()
    
    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart = cart, user = request.user)
    
    if order:
        request.session['order_id'] = order.order_id #order_id el que se creo en models con el pre_save