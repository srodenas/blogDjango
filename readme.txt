Algunos pasos
==============

1.- creamos el entorno virtual con virtualenv nombre-env y lo activamos con source
2.- Instalación de django
3.- creamos el proyecto con django-admin startproject nombre_proyecto
4.- creamos la app con python3 manage.py startapp aplicacion
5.- Registramos nuestra app dentro de las apps de settings
6.- Hacemos los modelos
7.- Instalar pilow y django-ckeditor
8.- Hacemos un python3 manage.py makemigrations
9.- Hacemos un python3 manage.py migrate
10.- Creamos un superusuario con python3 manage.py creatersuperuser
11.- Registramos nuestros modelos para la administración. abrimos admin.py y los Registramos
from .models import *
admin.site.register(Categoria)
12.- Configurar media para que las imágenes puedan subirse.
13.- Hay que incluir el urlpatter para que pueda verlas en mi navegador
14.- Importamos las plantilla en template y los css en static.
15.- Miramos en base, y añadirmos el nombre de nuestra carpeta templates.
16.- Dentro del index:
    añadimos el tag load staticfiles, porque hay que indicar a django, que ese
    html debe trabajar con ficheros estáticos, javascript, css.
    En todas las referencias a css y javascript, hay que incluir el tag static