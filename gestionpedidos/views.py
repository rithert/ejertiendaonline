from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from gestionpedidos.models import Articulos

#from django

# Create your views here.

def busqueda(request):
    return (render(request,'busqueda.html'))


def muestra_busqueda(request):
    if request.GET["producto"]:
        mensaje = "Se encontro los siguientes resultados para: " + request.GET["producto"]
        producto = request.GET["producto"]
        #articulos = Articulos.objects.filter(nombre__trigram_similar='martillo')
        articulos = Articulos.objects.filter(nombre__contains=producto)  
        return render(request,"resultados_busqueda.html",{"mensaje":mensaje,"articulos":articulos,"producto":producto})
    else:
        mensaje = "No se ingreso termino"
    return HttpResponse(mensaje)