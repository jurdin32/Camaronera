from django.db import models

# Create your models here.
from Inicio.models import Piscina
from Inventario.models import Producto


class Anio(models.Model):
    anio=models.CharField(max_length=4)

    def __str__(self):
        return self.anio

class Mes(models.Model):
    numero=models.IntegerField(default=0)
    anio=models.ForeignKey(Anio,on_delete=models.CASCADE)
    mes=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.mes

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        mm = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
              "Noviembre", "Diciembre"]
        self.mes=mm[self.numero]
        super(Mes, self).save()
class Dias(models.Model):
    mes=models.ForeignKey(Mes,on_delete=models.CASCADE)
    dia=models.DateField(unique=True)

    def __str__(self):
        return "%s"%self.dia

class Dietas(models.Model):
    dia=models.ForeignKey(Dias,on_delete=models.CASCADE)
    piscina=models.ForeignKey(Piscina,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return "%s"%self.dia

class DetalleDietas(models.Model):
    dieta=models.ForeignKey(Dietas,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.DecimalField(decimal_places=0, max_digits=9)

class Kardex(models.Model):
    fecha=models.DateField(null=True, blank=True)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    detalle_dieta=models.ForeignKey(DetalleDietas,on_delete=models.CASCADE,null=True,blank=True)
    tipo=models.CharField(max_length=20)
    cantidad=models.IntegerField(default=0)
    descripcion=models.TextField(null=True,blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            self.descripcion="Para registrar %s en el inventario de productos para la piscina %s de la empresa %s"%(self.tipo,self.detalle_dieta.dieta.piscina.slug,self.detalle_dieta.dieta.piscina.empresa.razon_social)
        except:
            pass
        super(Kardex, self).save()


