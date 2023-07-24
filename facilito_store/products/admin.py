from django.contrib import admin

# Register your models here.
from .models import Product

#poder configurar que cuando se agrege un producto solo aparescan estos atributos
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price','image')
    list_display = ('__str__','slug','created_at')

admin.site.register(Product,ProductAdmin)