from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Empresa(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    razon_social=models.CharField(max_length=200)
    ruc=models.CharField(max_length=13)
    direccion = models.TextField(null=True,blank=True)
    siglas = models.CharField(max_length=20,null=True,blank=True)
    fecha_apertura = models.DateField(null=True,blank=True)
    actividad = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)

    def __str__(self):
        return self.razon_social

class Piscina(models.Model):
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    numero=models.IntegerField(default=0)
    slug=models.CharField(max_length=100,null=True,blank=True)
    dimension=models.DecimalField(max_digits=9, decimal_places=4, default=0)
    precria=models.BooleanField(default=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.slug
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if Piscina.objects.count() == 0:
            self.numero = 1

        if self.numero==0:
            numeros=[]
            for i in Piscina.objects.all():
                numeros.append(i.numero)
            for i in range(Piscina.objects.count()+1):
                if not i+1 in numeros:
                    self.numero=i+1
                    break
        self.slug="PISCINA %s"%self.numero
        super(Piscina, self).save()
        

