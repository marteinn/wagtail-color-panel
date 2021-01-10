# Reference

## Panels

### NativeColorPanel

This panel uses the native `<input type="color"...` color selector (hence the name "native"). You use it by adding it to your page `content_panels`. It does not support IE11.

#### How to use

```python
from wagtail.core.models import Page
from wagtail_color_panel.edit_handlers import NativeColorPanel

class MyPage(Page):
    ...

    content_panels = Page.content_panels + [
        NativeColorPanel('my_color_field'),
    ]
```


### PolyfillColorPanel

This panel uses the third party package [Spectrum](https://github.com/bgrins/spectrum) as a color selector, the main purpose of this panel is to add IE11 support. You use it by adding it to your page `content_panels`.

#### How to use

```python
from wagtail.core.models import Page
from wagtail_color_panel.edit_handlers import PolyfillColorPanel

class MyPage(Page):
    ...

    content_panels = Page.content_panels + [
        PolyfillColorPanel('my_color_field'),
    ]
```


## Fields

### ColorField

A field based on CharField that only accept color values saved as hex values (example: `#CCCCCC`), its built to be compatible with `<input type="color"` so only 6-char hex values are supported. You still needs to define a panel for color selection.

#### How to use

```python
from wagtail.core.models import Page
from wagtail_color_panel.fields import ColorField

class MyPage(Page):
    my_color_field = ColorField()
```


## Blocks

### NativeColorBlock

This block uses the native `<input type="color"...` color selector (hence the name "native"). You use it by adding it to your page stream field blocks.

#### How to use

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
