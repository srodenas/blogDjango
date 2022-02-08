from django.urls import path
from .views import Inicio, CategoriaVideojuegos, CategoriaGenerales, FormularioContacto, DetallePost, Subcripciones


#añadimos una ruta para nuestra vista de clase

urlpatterns = [
    path ('', Inicio.as_view(), name='inicio'),
    path ('videojuegos/', CategoriaVideojuegos.as_view(), name='videojuegos'),
    path ('general/', CategoriaGenerales.as_view(), name='general'),
#podemos obtimizar código, utilizando sólo una vista y pasándole parámetros para que
#dentro de la vista, pueda seleccionar una opción y otra. Nos referimos a la distinción
#de las categorías. Eso se hace así:
# path ('videojuegos/', Categorias.as_view, {'categoria' : 'videojuegos'}, name='videojuegos')
# path ('general/', Categoria.as_view, {'categoria' : 'general'}, name='general')   
#Lo dejo para que lo modifiquéis vosotros mismos. 
    path ('formulario/', FormularioContacto.as_view(), name='contacto'),
    path('subcribirse/', Subcripciones.as_view(), name='subcripcion'),
    #path('subcripciones/', SubcripcionFuncion, name='subcripciones'),
    path('<slug:slug>/', DetallePost.as_view(), name='detallepost'),
   # path('subcribirse/', Subcripcion, name='subcripcion'),
    
]
