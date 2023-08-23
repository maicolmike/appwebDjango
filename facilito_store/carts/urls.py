from django.urls import path

from . import views

app_name = 'carts' #para establecer rutas

urlpatterns = [
    #path('<pk>',views.ProductDetailView.as_view(), name='product'), #id -> llave primaria
    path('', views.cart, name='cart'),
    path ('agregar', views.add, name='add'),
    path ('eliminar', views.remove, name='remove'),
]
