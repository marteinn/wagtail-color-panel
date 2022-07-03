from django.db import models
from wagtail import VERSION as WAGTAIL_VERSION

from wagtail_color_panel.blocks import NativeColorBlock
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.fields import ColorField

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import FieldPanel
    from wagtail.admin.panels import FieldPanel as StreamFieldPanel
    from wagtail.fields import StreamField
    from wagtail.models import Page
else:
    from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
    from wagtail.core.fields import StreamField
    from wagtail.core.models import Page


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
    body = (
        StreamField(
            [
                ("color", NativeColorBlock()),
            ],
            use_json_field=True,
        )
        if WAGTAIL_VERSION >= (3, 0)
        else StreamField(
            [
                ("color", NativeColorBlock()),
            ]
        )
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
