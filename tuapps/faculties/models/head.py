from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Dean(models.Model):
    faculty = models.ForeignKey(
        'faculties.Faculty',
        verbose_name=_('Faculty'),
        on_delete=models.CASCADE,
        related_name='deans'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    appointment_date = models.DateTimeField(default=timezone.now)
    termination_date = models.DateTimeField(default=timezone.now)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f'Dean of {self.faculty.name} - {self.user}'


class HeadOfDepartment(models.Model):
    department = models.ForeignKey(
        'faculties.Department',
        on_delete=models.CASCADE,
        related_name='%(class)ss'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    appointment_date = models.DateTimeField(default=timezone.now)
    termination_date = models.DateTimeField(default=timezone.now)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f'Head of department for {self.department.name} - {self.department.faculty.name}'


class HOD(HeadOfDepartment):
    class Meta:
        proxy = True

    def __str__(self):
        return f'HOD of {self.department} - {self.department.faculty}'
