from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
        help_text=_('Faculty position name')
    )
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'],
                name='unique_name_and_slug'
            )
        ]
        ordering = ['name']
