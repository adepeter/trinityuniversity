from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    FIRST_SEMESTER = 'f'
    SECOND_SEMESTER = 's'

    __SEMESTER_CHOICES = (
        (FIRST_SEMESTER, _('first semester')),
        (SECOND_SEMESTER, _('second semester')),
    )

    department = models.ForeignKey(
        'faculties.Department',
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    level = models.ForeignKey(
        'academics.Level',
        on_delete=models.CASCADE,
        related_name='courses'
    )
    unit = models.PositiveSmallIntegerField(
        default=1
    )
    semester = models.CharField(
        max_length=1,
        choices=__SEMESTER_CHOICES,
        default=FIRST_SEMESTER,
        help_text=_('semester course is been taught')
    )
    lecturers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f'{self.code} - {self.title}'


class Topic(models.Model):
    course = models.ForeignKey(
        'academics.Course',
        on_delete=models.CASCADE,
        related_name='topics'
    )
    taught_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name
