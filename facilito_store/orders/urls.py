from django.urls import path

from . import views

app_name = 'orders' #para establecer rutas

urlpatterns = [
    path('', views.order, name='order'),
]
