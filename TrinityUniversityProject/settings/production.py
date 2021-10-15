import os

from .base import *

SECRET_KEY = os.environ.get('STATESNG_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('TU_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('TU_DB_NAME', 'tu_db'),
        'USER': os.environ.get('TU_DB_USER', 'tu_user'),
        'PASSWORD': os.environ.get('TU_DB_PASSWORD', 'tu_password'),
        'HOST': os.environ.get('TU_DB_HOST', 'localhost'),
        'PORT': os.environ.get('TU_DB_PORT', '5432')
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True
