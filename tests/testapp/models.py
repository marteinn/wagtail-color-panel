from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.blocks import NativeColorBlock


class PageWithColorField(Page):
    color = ColorField()

    content_panels = Page.content_panels + [
        NativeColorPanel('color'),
    ]


class PageWithCharColorField(Page):
    color = models.CharField(max_length=7)


class PageWithDefaultValue(Page):
    color = ColorField(default="#FF0000")


class PageWithStreamfield(Page):
    body = StreamField([
        ('color', NativeColorBlock()),
    ])
