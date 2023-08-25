from django.db import models

# Create your models here.
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
import uuid

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE) #UNO A MUCHOS
    products = models.ManyToManyField(Product) # muchos a muchos
    subtotal = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    def update_totals(self): #va con update_totals
        self.update_subtotal()
        
    def update_subtotal(self):
        self.subtotal = [ product.price for product in self.products if product.all()]
    
def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action,*args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

pre_save.connect(set_cart_id, sender=Cart)