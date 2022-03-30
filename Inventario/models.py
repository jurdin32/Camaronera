from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=300)
    descripcion=models.CharField(max_length=300)

    def __str__(self):
        return self.nombre

class SubCategoria(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre


class Presentacion(models.Model):
    nombre=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre

class UnidadMedida(models.Model):
    presentacion=models.ForeignKey(Presentacion,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=300)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    subcategoria=models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    presentacion=models.ForeignKey(Presentacion,on_delete=models.CASCADE)
    peso=models.DecimalField(decimal_places=4, max_digits=9)
    forma_aplicacion=models.CharField(max_length=100, default="1")
    unidad=models.ForeignKey(UnidadMedida,on_delete=models.CASCADE)
    stock_minimo=models.DecimalField(decimal_places=4, max_digits=9)
    costo=models.DecimalField(decimal_places=4, max_digits=9)
    estado=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to='imagenes/',null=True,blank=True)

    def __str__(self):
        return self.nombre
