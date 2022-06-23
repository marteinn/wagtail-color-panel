from django.db import models
from wagtail import VERSION as WAGTAIL_VERSION

from wagtail_color_panel.blocks import NativeColorBlock
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.fields import ColorField

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.fields import StreamField
    from wagtail.models import Page
else:
    from wagtail.core.fields import StreamField
    from wagtail.core.models import Page


class PageWithColorField(Page):
    color = ColorField()

    content_panels = Page.content_panels + [
        NativeColorPanel("color"),
    ]


class PageWithCharColorField(Page):
    color = models.CharField(max_length=7)


class PageWithDefaultValue(Page):
    color = ColorField(default="#FF0000")


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
