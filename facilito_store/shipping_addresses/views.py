from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import ShippingAddress

class ShippingAddressListView(ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'
    
    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')