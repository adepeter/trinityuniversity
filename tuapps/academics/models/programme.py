from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Programme(models.Model):
    name = models.CharField(
        verbose_name=_('Programme name'),
        max_length=255
    )
    slug = models.SlugField(
        verbose_name=_('URL Identifier'),
        db_index=True,
        unique=True,
        help_text=_('Unique URL Identifier')
    )
    start_date = models.DateTimeField(
        verbose_name=_('Programme start date'),
        default=timezone.now,
        help_text=_('Date Programme was started')
    )

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'],
                name='unique_name_on_slug'
            )
        ]
        ordering = ['name']
