from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        unique=True,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        unique=True,
        blank=True,
        help_text=_('Unique URL Identifier')
    )
    description = models.TextField(blank=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Categories')
