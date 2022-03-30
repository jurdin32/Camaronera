from django.contrib import admin

# Register your models here.
from Camaronera.snniper import Attr
from Inventario.models import *


@admin.register(Categoria)
class modelo(admin.ModelAdmin):
    list_display = Attr(Categoria)
    list_display_links = Attr(Categoria)
    ordering = ['nombre']


@admin.register(SubCategoria)
class modelo(admin.ModelAdmin):
    list_display = Attr(SubCategoria)
    list_display_links = Attr(SubCategoria)
    ordering = ['nombre']

class UnidadInline(admin.StackedInline):
    model=UnidadMedida
    extra = 0

@admin.register(Presentacion)
class modelo(admin.ModelAdmin):
    list_display = Attr(Presentacion)
    list_display_links = Attr(Presentacion)
    ordering = ['nombre']
    inlines = [UnidadInline]

@admin.register(UnidadMedida)
class modelo(admin.ModelAdmin):
    list_display = Attr(UnidadMedida)
    list_display_links = Attr(UnidadMedida)

@admin.register(Producto)
class modelo(admin.ModelAdmin):
    list_display = Attr(Producto)
    list_display_links = Attr(Producto)