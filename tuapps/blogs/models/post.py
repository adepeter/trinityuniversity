from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.db import models


class Post(models.Model):
    article = models.ForeignKey(
        'blogs.Article',
        verbose_name=_('Category'),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    poster = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('poster'),
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True
    )
    content = models.TextField(
        verbose_name=_('content')
    )
    is_hidden = models.BooleanField(
        verbose_name=_('is hidden'),
        default=False,
        help_text=_('Determine if article can be listed')
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        related_name='children',
        blank=True,
        null=True
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
