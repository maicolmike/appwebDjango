from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from orders.common import OrderStatus
from stripeAPI.customer import create_customer

class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @property
    def shipping_address(self): #la direccion principal del usuario
        return self.shippingaddress_set.filter(default=True).first()
    
    @property
    def description(self):
        return 'Descripción para el usuario {}'.format(self.username)
    
    def has_customer(self):
        return self.customer_id is not None
    
    def create_customer_id(self):
        if not self.has_customer():
            customer = create_customer(self)
            self.customer_id = customer.id
            self.save()
    
    def has_shipping_address(self): # pose o no una direccion principal
        return self.shipping_address is not None
    
    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

    def has_shipping_addresses(self): # si el usuario posee direcciones
        return self.shippingaddress_set.exists()
    
    @property
    def addresses(self):
        return self.shippingaddress_set.all()
    
class Customer(User):  #proxy model
    class Meta:
        proxy=True
        
    def get_products(self):
        return []
    
class Profile(models.Model): #relacion on a on
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()