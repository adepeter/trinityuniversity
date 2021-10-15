from .base import *

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tu_db',
        'USER': 'tu_user',
        'PASSWORD': 'tu_password',
        'HOST': 'postgres',
        'PORT': 5432
    }
}
