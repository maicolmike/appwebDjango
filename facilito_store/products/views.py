from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

from django.db.models import Q # poder hacer filtro multiples

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('id')
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['products']=context['product_list']

        return context
    
class ProductDetailView(DetailView): #id - pk
    model = Product
    template_name = 'products/product.html' #esta fuera del snippets
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

        return context
    
class ProductSearchListView(ListView):
    template_name = 'products/search.html' #esta fuera del snippets
    
    def get_queryset(self):
        #SELECT * FROM products WHERE title like %valor%
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())  # busca por el titulo del producto o por el titulo de la categoria
        return Product.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count() # contar resultados

        return context