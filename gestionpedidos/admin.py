from django.contrib import admin
from gestionpedidos .models import Clientes,Articulos,Pedidos



# Register your models here.



class ClientesAdmin(admin.ModelAdmin):      #docuemnatcion django admin
    #fields = ('nombre','email')            #que registros se van a ingresar
    list_display = ('nombre','email')       #modificar lo que se ve cuando lista los registros
    search_fields = ('nombre','telefono')   #añadir cuador de busqueda para nombre y telefono
    
class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ('seccion',)              #filtros esto por seccuion

class PedidosAdmin (admin.ModelAdmin):
    list_display = ('numero','fecha')
    list_filter = ('fecha',) 
    date_hierarchy = 'fecha'                #navegacion horizontal derecha         


admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)
