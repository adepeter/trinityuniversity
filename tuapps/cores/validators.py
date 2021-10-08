from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_image_size(image, size):
    if size > image.size:
        raise ValidationError(_('Image is too large'), code='image_too_large')
