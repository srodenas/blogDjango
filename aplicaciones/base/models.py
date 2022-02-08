from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
'''
# ------Todos nuestros modelos, deben heredar en base de models.models----
* En fecha_creación y fecha_eliminación
    * auto_now lo ponemos a False, para que no deje constancia cada vez que modifico
un modelo. 
    * auto_now_add lo ponemos a True, para que deje constancia de la fecha de creación
cuando un modelo es creado.
* En fecha_modificación
    * auto_now lo ponemos a True
    * auto_now_add lo ponemos a False
* Será un modelo abstracto para que el resto heredan del mismo sin tener
que crear una tabla en la BBDD.
'''
class ModeloBase(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now = True, auto_now_add = False)
    fecha_eliminación = models.DateField('Fecha de eliminación', auto_now = False, auto_now_add = True)

    class Meta:
        abstract = True


'''
* Hereda de modeloBase
'''
class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la categoria', max_length = 100, unique = True)
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    #Cómo queremos ver los datos de las categorías.
    def __str__(self):
        return self.nombre

class Autor(ModeloBase):
    nombre = models.CharField('Nombre del autor', max_length=100)
    apellidos = models.CharField('Apellidos del autor', max_length = 150)
    email = models.EmailField('Email', max_length=200)
    descripcion = models.TextField('Descripcion')
    imagen_referencial = models.ImageField('Imagen del autor', null = True, blank = True, upload_to = 'autores/')
    web = models.URLField('Web del autor', null = True, blank = True)
    facebook = models.URLField('facebook del autor', null = True, blank = True)
    twitter = models.URLField('twitter del autor', null = True)
    istagram = models.URLField('Istagram del autor', null = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombre)

'''
    * Con imagen_referencial, utilizamos una imagen a subir a la carpeta imagenes
    Si no está creada la carpeta imagenes, lo creará automaticamente
    El autor será una clave Foránea, es decir que cada Post tendrá un autor y si
    borramos el autor, también se borrará en cascada los post de ese autor.
    autor(1) ----- (0-n)Post
    categoria(1) ----- (0-n)Post
    * Utilizaremos un editor de textos para los post. Eso lo podemos obtener
    con django-ckeditor. Hay que instarlo con pip3 install django-ckeditor
    *Debemos de registrarlo como aplicación, por tanto en INSTALLER_APPS, añadimos
    tanto el ckeditor como nuestra aplicación. Ahora debemos importar de 
    from ckeditor.fields import RichTextField. Añadimos el campo contenido del tipo
    RichTextField()
'''
class Post(ModeloBase):
    titulo = models.CharField('titulo del post', max_length=150, unique = True)
    slug = models.CharField('slug', max_length=150, unique = True)
    descripcion = models.TextField('descripcion')
    autor = models.ForeignKey(Autor, on_delete =models.CASCADE)
    #models.ForeignKey  on_delete = models.CASCADE
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagenes', upload_to='imagenes/', max_length=255)
    publicado = models.BooleanField('Publicado/No publicado', default = False)
    fecha_publicacion = models.DateField('Fecha de publicacion', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo


'''
    * Este modelo lo tenemos para información dinámica de nuestra web.
'''
class Web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Telefono', max_length=10)
    email = models.EmailField('Email', max_length=254)
    direccion = models.CharField('Dirección', max_length=200)
    
    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'
        
    def __str__(self):
        return self.nosotros
    
class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('istagram')
    
    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        
    def __str__(self):
        return self.facebook
    
    
    
class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    #nombre = models.CharField(max_length=100, verbose_name="Mi nombre")
    apellidos = models.CharField('Apellidos', max_length=150)
    correo =models.EmailField('Email', max_length=254)
    asunto = models.CharField('Asunto', max_length=100)
    mensaje = models.TextField('Mensaje')
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        
    def __str__(self):
        return self.asunto
   
   
class Supcriptor(ModeloBase):
    correo = models.EmailField('Email', max_length=254)
    
    class Meta: 
        verbose_name = 'Subcriptor'
        verbose_name_plural = 'Subcriptores'
        
    def __str__(self):
        return self.correo
    
    
    
