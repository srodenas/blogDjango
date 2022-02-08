
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#debemos indicar donde se encuentra nuestro directorio de ficheros estáticos.
#en la carpeta static, se encuentran nuestros css y javascript
#Hay que indicarle a django donde se en encuentra la carpeta static.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

#Es la url de la carpeta media. http://localhost:8000/media/
#En media, tenemos los ficheros estáticos multimedia, por categoría e imagenes
MEDIA_URL   = '/media/'

#hay que indicarle a django, donde se encuentra la carpeta de media.
MEDIA_ROOT = BASE_DIR / 'media'


#STATICFILES_DIRS = (BASE_DIR,'static')

#MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

