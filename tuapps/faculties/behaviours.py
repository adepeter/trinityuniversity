from django.db import models


class FacultyProfileMixin(models.Model):
    email = models.EmailField(default='noreply@localhost', blank=True)
    phone = models.CharField(max_length=255, default='2348097799871', blank=True)

    class Meta:
        abstract = True
