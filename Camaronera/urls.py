"""Camaronera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Dieta.views import anioDieta, mesDieta, diaDieta, dieta, getdietasPiscina
from Inicio.views import dashboard, piscinas, empresas
from Inventario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name='dashboard'),


    path('category/',categoria,name='categoria'),
    path('subcategory/',subcategoria,name='subcategoria'),
    path('getsubcategory/<int:id>/',getsubcategorias,name='getsubcategorias'),
    path('getunidad/<int:id>/',getunidad,name='getunidad'),
    path('product/',productos,name='productos'),


    path('pisc/',piscinas,name='piscina'),
    path('business/',empresas,name='empresa'),

    path('yeardiet/',anioDieta,name='yeardiet'),
    path('month/<int:id>/',mesDieta,name='mesDieta'),
    path('day/<int:id>/',diaDieta,name='diaDieta'),

    path('diet/<int:id>/', dieta, name='dieta'),
    path('dieta/<int:id>/', getdietasPiscina, name='getdietasPiscina'),

    path('inventary/', inventario_existencias, name='inventario_existencias'),
    path('inventary/emp/', inventario_existencias_empresa, name='inventario_existencias_empresa'),




]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
