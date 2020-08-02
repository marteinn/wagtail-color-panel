# Adding panel to a page

### First create a page

```python
from wagtail.core.models import Page

class MyPage(Page):
    ...
```


### Create a field that represents your data

Define a ColorField that represents your color, in this example we call it `color`.

```python
from wagtail.core.models import Page
from wagtail_color_panel.fields import ColorField

class MyPage(Page):
    color = ColorField(default="#000000")
```

Note: ColorField is built on top of CharField, so its also possible to use `CharField(max_length=7, default="#000000")`. The downside is that you will lose the hexcolor validation.`


### Add a content panel to represent the field in the admin

```python
from wagtail.core.models import Page
from wagtail_color_panel.edit_handlers import NativeColorPanel


class MyPage(Page):
    color = ColorField(default="#000000")

    content_panels = Page.content_panels + [
        NativeColorPanel('color'),
    ]
```

We're done! After migration a color picker should appear.


### Full example

```python
from wagtail.core.models import Page

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel


class MyPage(Page):
    color = ColorField()

    content_panels = Page.content_panels + [
        NativeColorPanel('color'),
    ]
```
