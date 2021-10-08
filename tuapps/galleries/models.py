from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


def upload_to(instance, filename):
    if not instance.folder or instance.folder is None:
        return f'galleries/{filename}'
    ancestors = instance.folder.get_ancestors(include_self=True)
    folders = [root.name for root in ancestors]
    folders = '/'.join(folders)
    return f'galleries/{folders}/{filename}'


class Folder(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    description = models.TextField(blank=True)
    is_hidden = models.BooleanField(default=False)
    parent = TreeForeignKey(
        'self',
        verbose_name=_('root'),
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Folders')


class Gallery(models.Model):
    folder = models.ForeignKey(
        'galleries.Folder',
        on_delete=models.CASCADE,
        related_name='galleries',
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to=upload_to)
    caption = models.CharField(max_length=255)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['image']
        verbose_name_plural = _('Galleries')


class Media(models.Model):
    folder = models.ForeignKey(
        'galleries.Folder',
        on_delete=models.CASCADE,
        related_name='media',
        null=True,
        blank=True
    )
    file = models.FileField(upload_to=upload_to)
    caption = models.CharField(max_length=255)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return str(self.file)

    class Meta:
        ordering = ['file']
        verbose_name_plural = _('Media')
