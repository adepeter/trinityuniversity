from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models


class Job(models.Model):
    posted_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('Posted by'),
        on_delete=models.DO_NOTHING,
        related_name='jobs'
    )
    title = models.CharField(
        verbose_name=_('Job Title'),
        max_length=255
    )
    slug = models.SlugField(
        unique=True,
        db_index=True
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    is_closed = models.BooleanField(
        verbose_name=_('Close application'),
        default=False,
        help_text=_('Is job ads still open for application submission')
    )
    date_posted = models.DateTimeField(default=timezone.now)
    date_closing = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
