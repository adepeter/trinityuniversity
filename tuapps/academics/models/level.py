from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=10)
    short_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name
