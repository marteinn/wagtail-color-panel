import re

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


hex_triplet_validator = RegexValidator(
    re.compile("^#[A-Fa-f0-9]{6}$"),
    message=_("Enter a valid color hash."),
    code="invalid",
)
