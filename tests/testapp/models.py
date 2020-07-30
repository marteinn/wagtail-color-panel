from django.db import models
from wagtail.core.models import Page

from wagtail_color_panel.fields import ColorField


class PageWithColorField(Page):
    color = ColorField()


class PageWithCharColorField(Page):
    color = models.CharField(max_length=7)


class PageWithDefaultValue(Page):
    color = ColorField(default="#FF0000")
