from django.contrib.gis.geometry import json_regex
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from Dieta.models import Kardex
from Inicio.models import Empresa
from Inventario.models import *


def categoria(request):
    if request.POST:
        if request.GET.get('edit'):
            cat=Categoria.objects.get(id=request.GET.get('edit'))
            cat.nombre=request.POST.get('nombre')
            cat.descripcion=request.POST.get('descripcion')
            cat.save()
            print("se modifico..!!")
            return HttpResponseRedirect("/category/")
        else:
            cat=Categoria.objects.create(
                nombre=request.POST.get('nombre'),
                descripcion=request.POST.get('descripcion')
            )
            cat.save()
            print('se creo nuevo')
            return HttpResponseRedirect("/category/")
    elif request.GET.get('remove'):
        cat = Categoria.objects.get(id=request.GET.get('remove'))
        cat.delete()
        print("se elimino..!!")
        return HttpResponseRedirect("/category/")

    contexto={
        'categorias':Categoria.objects.all(),
    }
    return render(request,'categoria.html',contexto)

def subcategoria(request):
    if request.POST:
        if request.GET.get('edit'):
            subc=SubCategoria.objects.get(id=request.GET.get('edit'))
            subc.nombre=request.POST.get('nombre')
            subc.save()
            print("se modifico..!!")
            return HttpResponseRedirect("/subcategory/?id="+request.GET.get('id'))
        else:
            subc=SubCategoria.objects.create(
                nombre=request.POST.get('nombre'),
                categoria_id=request.GET.get('id')
            )
            subc.save()
            print('se creo nuevo')
            return HttpResponseRedirect("/subcategory/?id=" + request.GET.get('id'))
    elif request.GET.get('remove'):
        subc = SubCategoria.objects.get(id=request.GET.get('remove'))
        subc.delete()
        print("se elimino..!!")
        return HttpResponseRedirect("/subcategory/?id=" + request.GET.get('id'))

    contexto={
        'categoria':Categoria.objects.get(id=request.GET.get('id')),
        'subcategorias':SubCategoria.objects.filter(categoria_id=request.GET.get('id')),
    }
    return render(request,'subcategoria.html',contexto)

def getsubcategorias(request,id):
    data = serializers.serialize("json", SubCategoria.objects.filter(categoria_id=id).order_by('nombre'))
    return JsonResponse(data,safe=False)

def getunidad(request,id):
    data = serializers.serialize("json", UnidadMedida.objects.filter(presentacion_id=id).order_by('nombre'))
    return JsonResponse(data,safe=False)

def productos(request):
    if request.POST:
        product = Producto()
        if request.GET.get('edit'):
            product=Producto.objects.get(id=request.GET.get('edit'))
        product.nombre=request.POST.get('nombre')
        product.subcategoria_id=request.POST.get('subcategoria')
        product.presentacion_id=request.POST.get('presentacion')
        product.forma_aplicacion=request.POST.get('forma_aplicacion')
        product.peso=request.POST.get('peso')
        product.costo = request.POST.get('costo')
        product.unidad_id=request.POST.get('unidad')
        product.stock_minimo=request.POST.get('stock')
        if request.FILES.get('imagen'):
            product.imagen=request.FILES['imagen']
        product.save()
        return HttpResponseRedirect("/product/")
    elif request.GET.get('status'):
        product = Producto.objects.get(id=request.GET.get('status'))
        if product.estado:
            product.estado=False
        else:
            product.estado=True
        product.save()
        return HttpResponseRedirect("/product/")
    contexto={
        'productos':Producto.objects.all(),
        'categorias':Categoria.objects.all().order_by('nombre'),
        'presentacion':Presentacion.objects.all().order_by('nombre')
    }
    return render(request,'productos.html',contexto)

def inventario_existencias(request):
    products=Producto.objects.all()
    contexto={
        "productos":products,
    }
    return render(request,'existencias.html',contexto)

def inventario_existencias_empresa(request):
    products=None
    products = Kardex.objects.filter(producto_id=request.GET.get('id'))
    if request.GET.get('business'):
        products = products.filter(detalle_dieta__dieta__piscina__empresa_id=request.GET.get('business'))
    if request.GET.get('type'):
        products = products.filter(tipo=request.GET.get('type'))


    contexto={
        "productos":products,
        "empresas":Empresa.objects.all(),
    }
    return render(request,'existencias_emp.html',contexto)