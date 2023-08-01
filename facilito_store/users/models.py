from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(User):
    class Meta:
        proxy=True
        
    def get_products(self):
        return []