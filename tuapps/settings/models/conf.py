from django.db import models
from django.utils.translation import gettext_lazy as _

from ..behaviours.conf import Configuration


class Setting(Configuration):
    title = models.CharField(
        verbose_name=_('site title'),
        max_length=20,
        default=_('Trinity University'),
        help_text=_('Website title')
    )
    description = models.TextField(
        verbose_name=_('site description'),
        blank=True,
        help_text=_('Website meta-tag description contents')
    )
    email = models.EmailField(
        verbose_name=_('e-mail'),
        default='noreply@localhost',
    )
    phone = models.CharField(max_length=255, blank=True, default='2348097799871')
    address = models.TextField(max_length=255, blank=True, default='State Specialist Hospital, Potiskum')
    welcome_mail = models.TextField(
        verbose_name=_('welcome message'),
        help_text=_('message after successful registration'),
        blank=True
    )
    facebook = models.URLField(blank=True, default='http://www.facebook.com/aderibigbep')
    twitter = models.URLField(blank=True, default='http://www.twitter.com/aderibigbep')
    linkedin = models.URLField(blank=True, default='http://www.linkedin.com/in/adepeter')
    instagram = models.URLField(blank=True, default='http://www.instagram.com/its_adepeter')
    is_under_maintenance = models.BooleanField(
        verbose_name=_('maintenance status'),
        null=True,
        help_text=_('Determine if site is under maintenance')
    )

    @property
    def is_under_construction(self):
        return self.is_under_maintenance
