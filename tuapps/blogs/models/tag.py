from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super().save(*args, **kwargs)
