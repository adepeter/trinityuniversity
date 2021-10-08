import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username):
    pattern = re.compile('^\w+$', re.I)
    if pattern.match(username) is None:
        raise ValidationError(
            _('Username contains invalid character(s)'),
            code='invalid_username_character'
        )