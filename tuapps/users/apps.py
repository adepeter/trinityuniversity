from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'tuapps.users'

    def ready(self):
        from . import signals
