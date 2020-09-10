from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)                 #char
    dirrecion = models.CharField(max_length = 50)
    email = models.EmailField()                             #email
    telefono = models.CharField(max_length=10)



class Articulos (models.Model):
    nombre = models.CharField(max_length=30)        
    seccion = models.CharField(max_length=30)
    valor = models.IntegerField(default=0)   


class Pedidos(models.Model):
    numero = models.IntegerField()                     #entero
    fecha = models.DateField()                          #fechas
    entregado = models.BooleanField()                    #booleano


