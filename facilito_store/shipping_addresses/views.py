from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import ShippingAddress
from .forms import ShippingAddressForm

from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required #vista basada en funciones
from django.contrib.auth.mixins import LoginRequiredMixin #vistas basada en clases
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from carts.utils import get_or_create_cart
from orders.utils import get_or_create_order
from django.http import HttpResponseRedirect

class ShippingAddressListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'
    success_message = 'Dirección actualizada exitosamente'
    
    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    login_url = 'login'
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'shipping_addresses/update.html'
    
    def get_success_url(self):
        return reverse('shipping_addresses:shipping_addresses')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')

        return super(ShippingAddressUpdateView, self).dispatch(request, *args, **kwargs)

class ShippingAddressDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_addresses/delete.html'
    success_url = reverse_lazy('shipping_addresses:shipping_addresses')
    
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('shipping_addresses:shipping_addresses')

        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')
        
        if self.get_object().has_orders(): #si el objeto posse ordenes retornar al listado de direcciones y no permitir que se elimine
            return redirect('shipping_addresses:shipping_addresses')

        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='login')
def create(request):
    form = ShippingAddressForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit = False) # metodo save se encargara de persisitir objeto
        shipping_address.user = request.user
        #shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists() # si no existen direcciones sera default
        shipping_address.default = not request.user.has_shipping_address() # si no existen direcciones sera default
        
        shipping_address.save()
        
        if request.GET.get('next'):
            if request.GET['next'] == reverse('orders:address'):
                cart = get_or_create_cart(request)
                order = get_or_create_order(cart, request)
                
                order.update_shipping_address(shipping_address)
                
                return HttpResponseRedirect(request.GET['next'])
            
        messages.success(request,'Dirreccion creada con exito')
        return redirect('shipping_addresses:shipping_addresses')
 
    return render(request, 'shipping_addresses/create.html',{
        'form': form
        
    }) 
    
@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    if request.user.has_shipping_address():
        request.user.shipping_address.update_default()

    shipping_address.update_default(True)

    return redirect('shipping_addresses:shipping_addresses')