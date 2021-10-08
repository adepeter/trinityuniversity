from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = _('Frequently asked question')
        verbose_name_plural = _('Frequently asked questions')
