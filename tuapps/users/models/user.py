import datetime
import uuid
from pathlib import PurePath

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ..managers.user import UserManager
from ..validators import validate_username
from ...cores.services.countries import get_countries
from ...cores.utils.string import stringify_uuid
from ...cores.utils.choice import Choicify


def upload_to(instance, filename):
    ext = PurePath(filename).suffix
    uuid4 = uuid.uuid4()
    filename = stringify_uuid(uuid4)
    ct = ContentType.objects.get_for_model(instance)
    app_name = ct.app_label
    app_model = ct.model
    return '%s/%s/%s%s' % (app_name, app_model, filename, ext)


countries_choices = Choicify(cache.get('countries_list', [('None', _('Please enter a country'))]))


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'

    __GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

    email = models.EmailField(
        verbose_name=_('e-mail'),
        unique=True
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=25,
        unique=True,
        db_index=True,
        validators=[validate_username]
    )
    gender = models.CharField(
        verbose_name=_('sex'),
        max_length=6,
        choices=__GENDER_CHOICES,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name=_('Profile picture'),
        null=True,
        blank=True,
        upload_to=upload_to
    )
    fullname = models.CharField(
        verbose_name=_('full name'),
        max_length=255,
        blank=True,
        null=True
    )
    about = models.TextField(
        verbose_name=_('About you'),
        help_text=_('Brief description of yourself'),
        blank=True
    )
    is_admin = models.BooleanField(
        verbose_name=_('Is admin'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Is superuser'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )
    telephone = models.CharField(
        verbose_name=_('Telephone'),
        max_length=20,
        blank=True,
        default='2348097799871'
    )
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=len(countries_choices),
        blank=True,
        null=True,
        choices=countries_choices.get_choices
    )
    date_created = models.DateTimeField(
        verbose_name=_('Registration date'),
        auto_now_add=True,
        help_text=_('Date and time of registration')
    )
    last_modified = models.DateTimeField(
        verbose_name=_('Last modified'),
        auto_now=True,
        help_text=_('Date and time of profile last modification')
    )
    last_seen = models.DateTimeField(
        verbose_name=_('Last time seen'),
        default=timezone.now,
        help_text=_('Date and time user was last active'),
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address'),
        blank=True,
        null=True,
        help_text=_('IP Address')
    )
    visits = models.PositiveIntegerField(default=0)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_constraint_user_email_username'
            )
        ]
        indexes = [
            models.Index(
                fields=['id', 'username'],
                name='idx_user_id_username'
            )
        ]
        ordering = ['email', 'username']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def get_short_name(self):
        return self.username

    @property
    def get_full_name(self):
        return self.email

    @property
    def dp(self):
        return self.profile_picture

    @property
    def display_name(self):
        if self.fullname is not None:
            return self.fullname
        return f'{self.get_short_name}'

    def last_seen_cache(self):
        return cache.get('seen_%s' % self.username)

    def is_online(self):
        if self.last_seen_cache():
            now = timezone.now()
            return now <= self.last_seen_cache() + \
                   datetime.timedelta(seconds=settings.USER_LASTSEEN_TIMEOUT)
        else:
            return False

    @property
    def profile_picture(self):
        return self.avatar.url

    def online(self):
        check_online = self.is_online()
        if check_online:
            return 'online'
        return 'offline'

    def get_absolute_url(self):
        kwargs = {
            'id': self.id,
            'username': slugify(self.username)
        }
        return reverse('tu:users:staff:staff_profile', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if self.gender is None and (self.avatar is None or not self.avatar):
            self.avatar = 'defaults/users/avatars/no_avatar.png'
        elif self.gender is self.GENDER_MALE and (self.avatar is None or not self.avatar):
            self.avatar = 'defaults/users/avatars/no_avatar_male.jpg'
        elif self.gender is self.GENDER_FEMALE and (self.avatar is None or not self.avatar):
            self.avatar = 'defaults/users/avatars/no_avatar_female.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name
