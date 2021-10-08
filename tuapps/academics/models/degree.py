from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Degree(models.Model):
    programme = models.ForeignKey(
        'academics.Programme',
        on_delete=models.CASCADE,
        related_name='%(class)ss'
    )
    faculty = models.ForeignKey(
        'faculties.Faculty',
        on_delete=models.CASCADE,
        related_name='%(class)ss'
    )
    department = models.ForeignKey(
        'faculties.Department',
        on_delete=models.CASCADE,
        related_name='%(class)ss'
    )
    courses = models.ManyToManyField(
        'academics.Course',
        verbose_name=_('Courses')
    )
    title = models.CharField(
        verbose_name=_('Degree type'),
        max_length=5,
        help_text=_('Designate degree title as either Bsc, Msc, PhD')
    )
    name = models.CharField(
        max_length=255,
        help_text=_('E.G Pure and Applied Chemistry')
    )
    start_date = models.DateTimeField(
        default=timezone.now,
        help_text=_('Date Degree was started in the institution')
    )
    preview = models.ImageField(
        upload_to='academics/degree',
        blank=True,
        default='defaults/academics/awards.png'
    )

    def __str__(self):
        return f'{self.title} {self.name}'
