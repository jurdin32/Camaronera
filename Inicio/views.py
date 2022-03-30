from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Inicio.models import Piscina, Empresa


def dashboard(request):
    contexto={

    }
    return render(request, 'index.html', contexto)

def empresas(request):
    if request.POST:
        emp=Empresa()
        if request.GET.get('edit'):
            emp=Empresa.objects.get(id=request.GET.get('edit'))
        emp.usuario=request.user
        emp.razon_social=request.POST.get('razon_social')
        emp.ruc=request.POST.get('ruc')
        emp.direccion=request.POST.get('direccion')
        emp.siglas=request.POST.get('siglas')
        emp.fecha_apertura=request.POST.get('fecha')
        emp.actividad=request.POST.get('actividad')
        if request.FILES.get('logo'):
            emp.logo=request.FILES['logo']
        emp.save()
        return HttpResponseRedirect('/business/')
    elif request.GET.get('status'):
        emp = Empresa.objects.get(id=request.GET.get('status'))
        emp.delete()
        return HttpResponseRedirect('/business/')
    contexto={
        'empresas':Empresa.objects.all(),
    }
    return render(request,'empresas.html',contexto)

def piscinas(request):
    if request.POST:
        print(request.POST,request.GET.get('edit'))
        pis=Piscina()
        if request.GET.get('edit'):
            print("editar",int(request.GET.get('edit')))
            pis=Piscina.objects.get(id=request.GET.get('edit'))
        pis.empresa_id=request.POST.get('empresa')
        pis.numero=request.POST.get('numero')
        pis.dimension=request.POST.get('dimension')
        if request.POST.get('precria'):
            pis.precria=True
        else:
            pis.precria=False
        if request.POST.get('estado'):
            pis.estado=True
        else:
            pis.estado=False
        pis.save()
        print("nuevo")
        return HttpResponseRedirect("/pisc/")
    elif request.GET.get('status'):
        print("estado",request.GET.get('status'))
        pis = Piscina.objects.get(id=request.GET.get('status'))
        if pis.estado:
            pis.estado=False
        else:
            pis.estado=True
        pis.save()
        return HttpResponseRedirect("/pisc/")
    piscin = Piscina.objects.all()
    contexto={
        'empresas':Empresa.objects.filter(usuario=request.user),
        'piscinas':piscin.order_by('-numero'),
        'contador':piscin.count()+1

    }
    return render(request,'piscinas.html',contexto)