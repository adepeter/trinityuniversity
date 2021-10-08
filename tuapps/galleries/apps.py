from django.apps import AppConfig


class GalleriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tuapps.galleries'

    def ready(self):
        from . import signals
