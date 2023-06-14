# Adding to a StreamField

To add the color chooser to a StreamField, import and use the `NativeColorBlock`.

```python
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail_color_panel.blocks import NativeColorBlock


class MyStreamFieldPage(Page):
    body = StreamField([
        ('color', NativeColorBlock(default="#000000")),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```
