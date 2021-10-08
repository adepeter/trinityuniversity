from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from martor.models import MartorField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from ..behaviours import FacultyProfileMixin


class Faculty(MPTTModel, FacultyProfileMixin):
    dean = models.OneToOneField(
        'faculties.Dean',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='+'
    )
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100, blank=True)
    long_description = MartorField(
        blank=True,
        default=_('No detailed description of faculty yet')
    )
    slug = models.SlugField(
        verbose_name=_('URL Identifier'),
        unique=True,
        db_index=True,
        help_text=_('Unique URL Identifier')
    )
    start_date = models.DateTimeField(default=timezone.now)
    programmes = models.ManyToManyField('academics.Programme')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )
    staffs = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='faculties.FacultyMembership',
        related_name='members'
    )

    @property
    def get_short_description(self):
        return self.short_description or 'No description yet'

    def get_absolute_url(self):
        kwargs = {
            'faculty': self.slug,
        }
        return reverse('tu:faculties:faculty_preview', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = str(f'{slugify(self.name)}@localhost.com')
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Faculties')


class FacultyMembership(models.Model):
    staff = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='faculty_memberships'
    )
    position = models.ForeignKey(
        'settings.Position',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    faculty = models.ForeignKey(
        'faculties.Faculty',
        on_delete=models.CASCADE,
        related_name='faculty_memberships'
    )
    department = models.ForeignKey(
        'faculties.Department',
        on_delete=models.CASCADE,
        related_name='faculty_memberships'
    )
    date_joined = models.DateTimeField(default=timezone.now)
