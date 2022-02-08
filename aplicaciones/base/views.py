from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from .models import *
from .consultasOrm import *
import random
from django.core.paginator import Paginator
from .formulario import ContactoFormulario
from django.core.mail import send_mail
from blogsanti.configuracion.base import EMAIL_HOST_USER


from django.http import HttpResponse

'''
Importamos ListView, porque voy a rederiar una lista
de registros.

'''

class Inicio(ListView):
       
    def get(self, request, *args, **kwargs):
        
        listaPost = devListaIdPosts()
        #print(listaPost)
        #le paso a random una secuencia y para ello, tengo que llamar al método choice
        idPrincipal = random.choice(listaPost) # Sacamos el id principal
        listaPost.remove(idPrincipal)
        
        id1 = random.choice(listaPost) #sacamos el id del post1
        listaPost.remove(id1)
        id2 = random.choice(listaPost) #sacamos el id del post2
        listaPost.remove(id2)
        id3 = random.choice(listaPost) #sacamos el id del post3
        listaPost.remove(id3)
        id4 = random.choice(listaPost) #sacamos el id del post4
        listaPost.remove(id4)
        #print(id1,id2,id3,id4)
        
        #Recuperamos nuestro post Principal
        miPostPrincipal = consultaPost(idPrincipal)
        # miPostPrincipal = Post.objects.get(id = idPrincipal)

        #Recuperamos nuestro último post de videojuegos
        ultimoPostVideojuegos = consultaUltimoPostVideojuegos()
            
        #Hacemos lo mismo con el últimoPost de General
        ultimoPostGeneral = consultaUltimoPostGeneral()
        
        
        #Ahora tenemos que recuperar las redes sociales y Web
        nuestraWeb = consultaNuestraWeb()
        nuestrasRedes = consultaNuestrasRedes()
        
        contexto = {
            'postPrincipal' : miPostPrincipal,
            'post1' : consultaPost(id1),
            'post2' : consultaPost(id2),
            'post3' : consultaPost(id3),
            'post4' : consultaPost(id4),
            'postGeneral' : ultimoPostGeneral,
            'postVideojuegos' : ultimoPostVideojuegos,
            'nuestraWeb' : nuestraWeb,
            'nuestrasRedes' : nuestrasRedes,
        }
        
        print(miPostPrincipal.categoria)
        return render(request, 'index.html', contexto)
        

#Esta clase devolverá una lista de objetos a la página de categorías
#Realizaremos una paginación de post con el objeto Paginator.
class CategoriaVideojuegos(ListView):
    
    
    def get(self, request, *args, **kwargs):
        
        #recogemos la lista de post de videojuegos
        postVideojuegos = devListPostVideojuegos();
       
        #recogemos la categoria de videojuegos 
        categoriaVideojuegos = devCategoriaVideojuegos()
        
        

        #Vamos con la paginación. La idea es con el objeto Paginator, controlar la paginación.
        #Para ello, pasamos todos los postVideojuegos a nuestro paginator, junto con el número de paginaciones.
        #Necestimos recupear con el método get del request, la variable o número de página que el
        #usuario ha pulsado y con ese valor, se lo pasamos al iterator que seleccionará los post
        #que le volverá a enviar al usuario.
        # https://docs.djangoproject.com/en/4.0/topics/pagination/
        
        miPaginador = Paginator(postVideojuegos, 3)  #todos los post y paginamos de 3
        paginaSeleccionada = request.GET.get('pagina') #recuperamos la página seleccinada
        postVideojuegosPaginacion = miPaginador.get_page(paginaSeleccionada) #devolvemos los post correspondientes a la pagina seleccionada
        
        
        contexto = {
            'post' : postVideojuegosPaginacion,
            'nuestraWeb' : consultaNuestraWeb(),
            'nuestrasRedes' : consultaNuestrasRedes(),
            'categoria' : categoriaVideojuegos,
        }
        return render(request, 'categoria.html', contexto)
    
   
    
#vista que devuelve los post de General
class CategoriaGenerales(ListView):
        
    def get (self, request, *args, **kwargs):
       
       #post generales 
        postGeneral = devListPostGeneral()
        categoriaGeneral = devCategoriaGeneral()
       
       #Iterator en generales
        miPaginador = Paginator(postGeneral, 3)  #todos los post y paginamos de 3
        paginaSeleccionada = request.GET.get('pagina') #recuperamos la página seleccinada
        postGeneralesPaginacion = miPaginador.get_page(paginaSeleccionada) #devolvemos los post correspondientes a la pagina seleccionada
        
        contexto = {
            'post' : postGeneralesPaginacion,
            'nuestraWeb' : consultaNuestraWeb(),
            'nuestrasRedes' : consultaNuestrasRedes(),
            'categoria' : categoriaGeneral,
        }    
        #Renderezamos la misma plantilla, pero con un contexto diferente
        return render (request, 'categoria.html', contexto)
  
'''
#Ejercicio que deberéis modificar para utilizar una sola vista.      
class Categoria (ListView):
    
    # @categoria, sería el diccionario que le pasamos desde la llamada a la vista 
    # Categoria.as_view puesta dentro del fichero urls
    
    def get (self, request, categoria, *args, **kwargs):
        
'''


#Esta vista, renderizará un formulario de contacto.
class FormularioContacto(View):
    
    def get (self, request, *args, **kwargs):
        
        #Ahora tenemos que recuperar la info de la  Web
        nuestraWeb = consultaNuestraWeb()
        nuestrasRedes = consultaNuestrasRedes()
        
        #Necesitamos instanciar nuestro formulario de contacto
        formulario = ContactoFormulario()
        
        contexto = {
            'nuestraWeb' : nuestraWeb,
            'nuestrasRedes' : nuestrasRedes,
            'formularioContacto' : formulario,
        }
        
        print ('Nuestra web', nuestraWeb)
        return render(request, 'contacto.html', contexto)
    

#Necesitamos definir el método post delformulario de contacto
#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Forms
#validamos el post.
    
    def post(self, request, *args, **kargs):
        #recogemos el formulario a partir de la petición por método POST.
        formulario = ContactoFormulario(request.POST)
        #comprobamos si el formulario es válido.
        if formulario.is_valid():
            formulario.save()
            #hay que importar rediect al igual que render.
            return redirect('blog:inicio')
        else:
            #sino es correcto, debemos de devolver el formulario a la vista
            #contacto.html, por tanto renderizamos.
            
            contexto ={
                'formularioContacto ' : formulario,
            }
            return render(request, 'contacto.html', contexto)
             
             
#Implementaremos una clase para los detalles de cada uno de los post seleccionados.             
class DetallePost(DetailView):
    
    #@slug es el parámetro que diferencia un post de otro al pulsar su detalle.
    def get (self, request, slug, *args, **kargs):
        #obtendremos a partir del parámetro slug, voy a entrar a su detalle.
        #Leemos todos los post que coincidan con su slug dentro de un try
        #Crearemos nuestro contexto y añadimos el post junto a sociales y redes por la herencia
        #retornaremos el render a nuestro template post.html.
        #importamos la ruta path('<slug:slug>/', DetallePost.as_view(), name='detalle_post')
        
        try:
            post = Post.objects.get(slug = slug)
            print (post)
        except:
            post = None
            print ('No existe ese post')
            
        #Ahora tenemos que recuperar la info de la  Web
        nuestraWeb = consultaNuestraWeb()
        nuestrasRedes = consultaNuestrasRedes()
        
       #seleccionaré otros post que tengan que ver con la misma categoria
        otrosPost = Post.objects.filter(
            estado = True,
            publicado = True,
            
            
        ).values_list(flat = True)
        listaidPost = list(otrosPost)
        
        listaidPost.remove(post.id)  #eliminamos el post del detalle
        
        otroId1= random.choice(listaidPost)  #elegimos un post aleatorio
        listaidPost.remove(otroId1)    #lo quitamos de la lista
        otroId2= random.choice(listaidPost) #elegimos un segundo post aleatorio
        listaidPost.remove(otroId2)    #lo volvemos a quitar de la lista
        otroId3= random.choice(listaidPost) #elegimos un tercer post aleatorio
        
        listaPostAleatorios = [
            consultaPost(otroId1), 
            consultaPost(otroId2),
            consultaPost(otroId3)
        ]  #metemos los tres post en una lista.
        
        contexto = {
            'nuestraWeb' : nuestraWeb,
            'nuestrasRedes' : nuestrasRedes,
            'postDetalle' : post,
            'otrosPost' : listaPostAleatorios,
        }
        print (listaPostAleatorios)
        
        return render (request, 'post.html', contexto)
        
        

#Esta vista creará una supcripción y enviará un correo de agradecimiento.     
#Debemos de trabajar con django.core.mail import send_mail
#https://pywombat.com/articles/correos-django
#https://runebook.dev/es/docs/django/topics/email
  
'''
def SubcripcionFuncion(request):
    if (request.method=="POST"):
        respuesta = 'metodo post'
    else:
        respuesta = 'metodo get'
        
    
    return HttpResponse(respuesta)
'''
     
class Subcripciones(View):
    
    def get(self, request, *args, **kargs):
        print ('Método get')
        return redirect ('blog:inicio')
        #respuesta = "Acabamos de pulsar el método get"
        #return HttpResponse(respuesta)
    
    
    def post(self, request, *args, **kargs):        
        
        #recuperamos el contacto
        contacto = request.POST.get('correo')
        #insertamos en la bbdd
        Supcriptor.objects.create(correo = contacto)
        asunto = 'Gracias por su subcripcion'
        mensaje = 'Te agradezco tu subcripción, en breve recibirás nás notiticas'
        print ("correo: ", contacto," asunto: ", asunto," mandado desde  ", EMAIL_HOST_USER)
        
        try:
            remitente = EMAIL_HOST_USER
            send_mail(asunto, mensaje, remitente, [contacto],fail_silently=False,)
            print("No hay error de email")
        except:
            print ("error al enviar email")
            #pass
        
        return redirect ('blog:inicio')
   
   
   # def post(self, request, *args, **kargs):
        #recuperamos el campo del formulario
   #     print ('entro aquí en subcripcion')
        #return render (request, 'inicio.html',{})
        
       # correo = request.POST.get('correo')
        
       
        #print ('el correo es ', correo)
        
        #Doy de alta un registro en la bbdd.
        #Supcriptor.objects.create(correo = correo)
        #asunto = 'Gracias por su subcripcion'
        #mensaje = 'Te agradezco tu subcripción, en breve recibirás nás notiticas'
       # print ('el correo es ', correo)
      #  return redirect('blog:inicio')
        
        #try:
        #    remitente = EMAIL_HOST_USER
        #    send_mail(asunto, mensaje, remitente, [correo])
        #except:
        #    pass
        
        #return redirect('blog:inicio')
        
      #  return None
        
