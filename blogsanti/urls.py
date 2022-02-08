"""blogsanti URL Configuration

ESTA ES EL FICHERO DE RUTAS DE MI PROYECTO
TENEMOS QUE TRAER TODAS LAS RUTAS DE CADA 
UNA DE NUESTRAS APLICACIONES. PARA ELLO, DEBEMOS
DE IMPORTAR LA CLASE INCLUDE

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

#Asignamos al grupo de base.urls el nombre de base
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('aplicaciones.base.urls', 'blog'))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
Cada solicitud de url, debe encagar con las que tengamos
definidos en nuestra urlpatterns. si no encaja, no lo tramitara
y dara un error.
Por definición, cada url se asocia a una vista.
'''

#para que podemos ver las imagenes pinchando sobre su enlace
# es la expresión regular para que añada cualquier patrón con
# el nombre de la imagen y su ruta.
#https://docs.djangoproject.com/en/4.0/howto/static-files/#configuring-static-files

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve , {
            'document_root':settings.MEDIA_ROOT,
        }),
    ]
