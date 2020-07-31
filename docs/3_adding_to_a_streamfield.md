# Adding to a StreamField

To add the color chooser to a StreamField, import and use the `NativeColorBlock`.

```python
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock


class MyStreamFieldPage(Page):
    body = StreamField([
        ('color', NativeColorBlock(default="#000000")),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```
