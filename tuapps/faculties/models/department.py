from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ..behaviours import FacultyProfileMixin


class Department(FacultyProfileMixin):
    hod = models.OneToOneField(
        'faculties.HOD',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='+'
    )
    faculty = models.ForeignKey(
        'faculties.Faculty',
        on_delete=models.CASCADE,
        related_name='departments'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name=_('URL Identifier'),
        unique=True,
        db_index=True,
        help_text=_('Unique URL Identifier')
    )
    programmes = models.ManyToManyField('academics.Programme')
    start_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        kwargs = {
            'faculty': self.faculty.slug,
            'department': self.slug,
        }
        return reverse('tu:faculties:department_preview', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Departments')
