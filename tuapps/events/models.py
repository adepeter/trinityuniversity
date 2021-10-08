from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField

from precise_bbcode.fields import BBCodeTextField

from .managers import EventManager


class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = BBCodeTextField(default=_('Yet to define an event'))
    image = ResizedImageField(
        verbose_name=_('image'),
        upload_to='events',
        size=[950, 350],
        default='defaults/events/events_default.jpg',
        null=True,
        blank=True,
        help_text=_('Event cover image')
    )
    is_hidden = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = EventManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
