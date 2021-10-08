from django.db import models


class EventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)

    def hidden_events(self):
        return self.filter(is_hidden=True)
        
    def unhidden_events(self):
        return self.filter(is_hidden=False)
