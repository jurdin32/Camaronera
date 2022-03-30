from django.contrib import admin

# Register your models here.
from Camaronera.snniper import Attr
from Dieta.models import *


@admin.register(Dias)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Dias)
    list_display = Attr(Dias)

class DiasInline(admin.StackedInline):
    model=Dias
    extra = 0

@admin.register(Mes)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Mes)
    list_display = Attr(Mes)
    inlines = [DiasInline]

class MesInline(admin.StackedInline):
    model = Mes
    extra = 0

@admin.register(Anio)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Anio)
    list_display = Attr(Anio)
    inlines = [MesInline]


class DietasInline(admin.StackedInline):
    model = DetalleDietas
    extra = 0

@admin.register(DetalleDietas)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(DetalleDietas)
    list_display = Attr(DetalleDietas)


@admin.register(Dietas)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Dietas)
    list_display = Attr(Dietas)
    inlines = [DietasInline]

@admin.register(Kardex)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Kardex)
    list_display = Attr(Kardex)


