from django import template
from django.db.models import Sum

from Dieta.models import DetalleDietas, Kardex
from Inventario.models import Producto

register = template.Library()

@register.simple_tag
def calculo_stock(id):
    kardex=Kardex.objects.filter(producto_id=id)
    ingreso=kardex.filter(tipo="INGRESO").aggregate(Sum('cantidad'))['cantidad__sum']
    egreso = kardex.filter(tipo="EGRESO").aggregate(Sum('cantidad'))['cantidad__sum']
    if ingreso!=None:
        print(ingreso)
    else:
        ingreso=0
    if egreso !=None:
        print(egreso)
    else:
        egreso=0
    return (ingreso-egreso)