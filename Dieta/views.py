from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from Camaronera.snniper import obtener_dias_del_mes
from Dieta.models import Anio, Mes, Dias, Dietas, DetalleDietas, Kardex
from Inicio.models import Piscina
from Inventario.models import Producto


def meses(anio):
    result=[]
    for mm in Mes.objects.filter(anio_id=anio):
        result.append(mm.numero)
    print(result)
    for i in range(1, 13):
        if not i in result:
            Mes.objects.create(anio_id=anio,numero=i).save()

def obtenerFaltantes(anio):
    result = []
    lista=[]
    mm = ["----", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
          "Noviembre", "Diciembre"]
    for m in Mes.objects.filter(anio_id=anio):
        result.append(m.numero)
    for i in range(1, 13):
        if not i in result:
            lista.append({'n':i,'mes':mm[i]})
    return lista


def anioDieta(request):
    if request.POST:
        anio=Anio()
        if request.GET.get('edit'):
            anio=Anio.objects.get(id=request.GET.get('edit'))
        anio.anio=request.POST.get('anio')
        anio.save()
        return HttpResponseRedirect("/yeardiet/")
    elif request.GET.get('remove'):
        anio=Anio.objects.get(id=request.GET.get('remove'))
        anio.delete()
        return HttpResponseRedirect("/yeardiet/")
    contexto={
        'anios':Anio.objects.all()
    }
    return render(request,'anioDieta.html',contexto)

def mesDieta(request,id):
    if request.GET.get("generar"):
        meses(id)
        return HttpResponseRedirect("/month/%s/"%id)
    if request.POST:
        print(request.POST)
        if request.GET.get('new'):
            mes=Mes.objects.create(numero=int(request.POST.get('numero')),anio_id=id)
            mes.save()
            return HttpResponseRedirect("/month/%s/" % id)
    elif request.GET.get("remove"):
        mes=Mes.objects.get(id=request.GET.get("remove"))
        mes.delete()
        return HttpResponseRedirect("/month/%s/" % id)

    contexto={
        'meses':Mes.objects.filter(anio_id=id).order_by('numero'),
        'faltantes':obtenerFaltantes(id),
        'id':id,
    }
    return render(request,'mesDieta.html',contexto)

def diaDieta(request,id):
    mes=Mes.objects.get(id=id)
    print(mes.numero,mes.anio.anio)
    if request.GET.get('generar'):
        for i in range(obtener_dias_del_mes(mes.numero, int(mes.anio.anio))):
            try:
                dia=Dias.objects.create(
                    mes_id=mes.id,
                    dia='%s-%s-%s'%(mes.anio.anio,str.zfill(str(mes.numero),2),str.zfill(str(i+1),2))
                )
                dia.save()
            except:
                pass
    contexto={
        'dias':Dias.objects.filter(mes_id=id),
        'mes':mes,

    }
    return render(request,'diaDieta.html',contexto)

def getdietasPiscina(request,id):
    lista=[]
    for det in DetalleDietas.objects.filter(dieta_id=id):
        lista.append({"id":det.id,"producto":det.producto.nombre,"cantidad":det.cantidad,"id_prod":det.producto_id,"piscina":det.dieta.piscina.slug,"piscina_n":det.dieta.piscina.numero,'id_piscina':det.dieta.piscina_id})
    print(lista)
    return JsonResponse(lista,safe=False)

def dieta(request,id):
    productos=Producto.objects.filter(estado=True)
    dia=Dias.objects.get(id=id)
    if request.GET.get('piscina'):
        diet=Dietas()
        try:
            diet=Dietas.objects.get(dia_id=id,piscina_id=request.GET.get('piscina'))
        except:
            diet.dia=dia
            diet.piscina_id=request.GET.get('piscina')
            diet.save()
        dietaDet=DetalleDietas.objects.create(
            dieta_id=diet.id,
            producto_id=request.GET.get('producto'),
            cantidad=request.GET.get('cantidad'),
        )
        dietaDet.save()
        kardex=Kardex(producto_id=dietaDet.producto_id,detalle_dieta_id=dietaDet.id,tipo="EGRESO",cantidad=dietaDet.cantidad)
        kardex.save()
        print(kardex)
        return HttpResponse(diet.id)

    if request.GET.get('edit'):
        det = DetalleDietas.objects.get(id=request.GET.get('edit'))
        det.producto_id=request.GET.get('producto')
        det.cantidad=request.GET.get('cantidad')
        det.save()
        kardex=Kardex.objects.get(detalle_dieta_id=det.id)
        kardex.producto_id=det.producto_id
        Kardex.cantidad=det.cantidad
        kardex.save()

        return HttpResponse(det.dieta_id)

    if request.GET.get('remove'):
        det=DetalleDietas.objects.get(id=request.GET.get('remove'))
        det.delete()
        return HttpResponse("ok")

    contexto={
        'piscinas':Piscina.objects.all().order_by('id'),
        'productos':productos.order_by('subcategoria__categoria__nombre'),
        'dia':dia,
        'detalles':DetalleDietas.objects.filter(dieta__dia_id=id)
    }
    return render(request,'dietas.html',contexto)