from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtail_color_panel.blocks import NativeColorBlock
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.fields import ColorField


class PageWithColorField(Page):
    color = ColorField()

    content_panels = Page.content_panels + [
        NativeColorPanel("color"),
    ]


class PageWithCharColorField(Page):
    color = models.CharField(max_length=7)

    content_panels = Page.content_panels + [
        FieldPanel("color"),
    ]


class PageWithDefaultValue(Page):
    color = ColorField(default="#FF0000")

    content_panels = Page.content_panels + [
        NativeColorPanel("color"),
    ]


class PageWithStreamfield(Page):
    body = StreamField(
        [
            ("color", NativeColorBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
