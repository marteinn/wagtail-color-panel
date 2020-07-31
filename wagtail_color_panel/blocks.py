from django import forms
from django.utils.functional import cached_property
from wagtail.core.blocks import FieldBlock

from wagtail_color_panel.widgets import ColorInputWidget
from wagtail_color_panel.validators import hex_triplet_validator


class NativeColorBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, validators=(), **kwargs):
        self.field_options = {
            "required": required,
            "help_text": help_text,
            "max_length": 7,
            "min_length": 7,
            "validators": [hex_triplet_validator],
        }
        super().__init__(**kwargs)

    @cached_property
    def field(self):
        field_kwargs = {"widget": ColorInputWidget()}
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    class Meta:
        icon = "radio-full"
