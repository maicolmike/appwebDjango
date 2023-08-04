from django.db import models

# Create your models here.
from users.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE) #UNO A MUCHOS
    products = models.ManyToManyField(Product) # muchos a muchos
    subtotal = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return ''