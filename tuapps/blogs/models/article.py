from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.db import models
from django_resized import ResizedImageField


class Article(models.Model):
    category = models.ForeignKey(
        'blogs.Category',
        verbose_name=_('Category'),
        on_delete=models.CASCADE,
        related_name='articles'
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_('author'),
        on_delete=models.SET_NULL,
        related_name='articles',
        null=True
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        unique_for_date='date_posted'
    )
    cover = ResizedImageField(
        upload_to='blogs/articles',
        size=[950, 350],
        blank=True,
        null=True,
        default='defaults/blogs/blog_default.jpeg'
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        help_text=_('Unique URL Identifier'),
        blank=True
    )
    content = models.TextField(
        verbose_name=_('content')
    )
    is_locked = models.BooleanField(
        verbose_name=_('is locked'),
        default=False,
        help_text=_('Determine if article can be modified')
    )
    is_hidden = models.BooleanField(
        verbose_name=_('is hidden'),
        default=False,
        help_text=_('Determine if article can be listed')
    )
    tags = models.ManyToManyField(
        'blogs.Tag',
        blank=True
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def get_preview_cover(self):
        return self.cover.url

    @property
    def short_content(self):
        return self.content[:20]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            'id': self.id,
            'slug': self.slug,
        }
        return reverse('tu:blogs:article_read', kwargs=kwargs)

    def __str__(self):
        return self.title
