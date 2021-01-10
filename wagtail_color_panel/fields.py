from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail_color_panel.validators import hex_triplet_validator


class ColorField(models.CharField):
    default_validators = [hex_triplet_validator]
    description = _("Hex triplet colors")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)
