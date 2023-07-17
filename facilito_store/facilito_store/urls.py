
from django.contrib import admin
from django.urls import path

from . import views

from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    #definir url
    #path('',views.index, name='index'),
    path('',ProductListView.as_view(), name='index'),
    path('usuarios/login',views.login_view, name='login'),
    path('usuarios/logout',views.logout_view, name='logout'),
    path('usuarios/registro',views.register, name='register'),
]
