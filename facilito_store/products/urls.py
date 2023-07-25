from django.urls import path

from . import views

urlpatterns = [
    #path('<pk>',views.ProductDetailView.as_view(), name='product'), #id -> llave primaria
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>',views.ProductDetailView.as_view(), name='product'), #id -> llave primaria
    
]
