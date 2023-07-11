
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #definir url
    path('',views.index, name='index'),
    path('usuarios/login',views.login_view, name='login'),
]
