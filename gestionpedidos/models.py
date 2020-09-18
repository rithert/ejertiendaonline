from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30,verbose_name="El nombre")                 #char
    dirrecion = models.CharField(max_length = 50)
    email = models.EmailField(blank=True,null=True)                             #email
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre 



class Articulos (models.Model):
    nombre = models.CharField(max_length=35)        
    seccion = models.CharField(max_length=30)
    valor = models.IntegerField(default=0)
    def __str__(self):
        return '(nombre = '+self.nombre+',seccion = '+self.seccion+',valor = '+ str(self.valor)+')'


class Pedidos(models.Model):
    numero = models.IntegerField()                     #entero
    fecha = models.DateField()                          #fechas
    entregado = models.BooleanField() 
    
    def __str__(self):
        return str(self.numero)                  #booleano


