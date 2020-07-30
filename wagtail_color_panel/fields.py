import re

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


hex_triplet_validator = RegexValidator(
    re.compile('^#[A-Fa-f0-9]{6}$'),
    message=_('Enter a valid color hash.'),
    code='invalid',
)


class ColorField(models.CharField):
    default_validators = [hex_triplet_validator]
    description = _("Hex triplet colors")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)
