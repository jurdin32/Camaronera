from django.contrib import admin

# Register your models here.
from Camaronera.snniper import Attr
from Inicio.models import *


@admin.register(Empresa)
class modelo(admin.ModelAdmin):
    list_display = Attr(Empresa)
    list_display_links = Attr(Empresa)

@admin.register(Piscina)
class modelo(admin.ModelAdmin):
    list_display = Attr(Piscina)
    list_display_links = Attr(Piscina)
    ordering = ['numero']
    readonly_fields = ['slug',]