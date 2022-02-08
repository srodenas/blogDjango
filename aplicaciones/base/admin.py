from django.contrib import admin
from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'estado', 'fecha_creacion')
    search_fields = ['nombre']
    

class AutorAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellidos', 'email', 'estado')
    search_fields = ['nombre', 'apellidos']

class PostAdmin(admin.ModelAdmin):
    list_display=('titulo','descripcion','autor','categoria','contenido','estado','publicado','fecha_publicacion')
    search_fields = ['titulo','slug']
    
class WebAdmin(admin.ModelAdmin):
    list_display=('nosotros','telefono','email','direccion','estado')
    search_fields = ['nosotros']
    
class RedesSocialesAdmin(admin.ModelAdmin):
    list_display=('facebook','twitter','instagram','estado')
    search_fields=['facebook','twitter','instagram']
    
class ContactoAdmin(admin.ModelAdmin):
    list_display=('nombre','apellidos','correo','asunto','mensaje')
    search_fields=['correo']
    
class SubcriptorAdmin(admin.ModelAdmin):
    list_display=('correo',)
    search_fields=['correo']
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(RedesSociales, RedesSocialesAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Supcriptor, SubcriptorAdmin)



#Vamos a añadir botones de importación/exportación de los datos y mostrar más información
#Para ello, hay que instalar el paquete import_export de la forma:

#pip3 install django-import-export

#Hay que añadirlo en nuestro archivo base de aplicaciones de la forma 'import_export'
#Después hay que importar from import_export import resources
#También importar from impor_export.admin import ImportExportModelAdmin

#Para cada clase, hay que heredar de una clase del tipo resources.ModelResource y definir la meta
#También vamos a personalizar los campos dentro del panel de administración

#https://www.youtube.com/watch?v=B8Dxz3PO80k   (vídeo 18). Para cambiar campos en el panel de administración)

#Crearemos una clase que herede de ModelAdmin, que permite hacer modificaciones en nuestros modelos
#del panel de administración. Lo haremos antes de registrar la clase.
