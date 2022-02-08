from .models import *


'''
        # recuperamos los post utilizando un filtro. Hay que importar el modelo Post
        y el ORM, se encarga de objeter todos los registros convertidos en objetos dentro
        de un QuerySet de python. Para ello, llamamos a objects y con filter le decimos que filtre
        cuando los atributos estado y publicado estén en true. El QuerySet, debe de tener como datos
        una lista con sólo los id.
        #Después, hemos convertido el QuerySet a una lista, para ello hacemos el cast a list
        #Ahora, queremos generar id aleatorios y para ello, utilizando ramdon cogiendo un valor
        aleatorio de los que hay en la lista y después lo vamos sacando para volver a generar un total
        de 4 aleatorios por cada carga de la vista, para que salgan los post diferentes en cada request.
        '''
def devListaIdPosts():
    misPost = Post.objects.filter(
            estado = True,
            publicado = True
            ).values_list('id', flat = True)
    listaPost = list(misPost)
    return listaPost


#Devuelve todos los post de la categoría Videojuegos
def devListPostVideojuegos():
    misPost = Post.objects.filter(
        estado = True,
        publicado = True,
        categoria = Categoria.objects.get(nombre = 'Videojuegos')
    )
    return misPost




#Devuelve la categoría de Videojuegos
def devCategoriaVideojuegos():
    try:
        categoria = Categoria.objects.get(nombre = 'Videojuegos')
    except:
        categoria = None
        print ('No existe la categoria Videojuegos')
    return categoria



#Devuelve la lista de los post Generales
def devListPostGeneral():
    postGenerales = Post.objects.filter(
        estado = True,
        publicado = True,
        categoria = Categoria.objects.get(
                nombre = 'General'
        )
    )
    return postGenerales



#Devuelve la categoria Genral      
def devCategoriaGeneral():
    try:
            categoriaGeneral = Categoria.objects.get(
                nombre = 'General'
            )
    except:
        categoriaGeneral = None
        print ('No existe la categoria general')    
    
    return categoriaGeneral  
        
       

#devuelve un post donde el id es pasado por referencia
def consultaPost(id1):
    return Post.objects.get(id = id1)



    '''
        Ahora necesitamos recuperar los post por categoría videojuegos y general.
        Por si acaso no tenemos cualquiera de las categorías, lo encerraremos
        en un bloqu try except. Pasaremos la última según la fecha de 
        publicación.
        
    '''
def consultaUltimoPostVideojuegos():
    try:
        ultimoPostVideojuegos = Post.objects.filter(
            estado = True,
            publicado = True,
            categoria = Categoria.objects.get(
                    nombre = 'Videojuegos'
            )
        ).latest('fecha_publicacion')
                
    except:
        ultimoPostVideojuegos = None
        print("No existe la categoría Videojuegos")
    return ultimoPostVideojuegos



def consultaUltimoPostGeneral():
    try:
        ultimoPostGeneral = Post.objects.filter(
            estado = True,
            publicado = True,
            categoria = Categoria.objects.get(
                nombre = 'General'
            )
        ).latest('fecha_publicacion')
                    
    except:
        ultimoPostGeneral = None
        print("No existe la categoria General")
    return ultimoPostGeneral



def consultaNuestraWeb():
    return Web.objects.filter(estado = True).latest('fecha_modificacion')
    
def consultaNuestrasRedes():
    return RedesSociales.objects.filter(estado = True).latest('fecha_modificacion')
