![Wagtail-Color-Panel](https://github.com/marteinn/wagtail-color-panel/workflows/Wagtail-Color-Panel/badge.svg)

# Wagtail-Color-Panel

Introduces a color field and panel to Wagtail.


## Features

- ColorPanel that can be used in your edit handler
- ColorBlock for usage in a StreamField
- Based on the native HTML5 color picker
- A custom db field for easier conversion from hexadecimal colors to other formats (such as RGB)


## Examples

### As a edit_handler

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


### As a StreamField block

```python
from wagtail.core.models import Page
from wagtail_color_panel.blocks import ColorBlock


class PageWithStreamfield(Page):
    body = StreamField([
        ('color', ColorBlock()),
    ])
```


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-Color-Panel is released under the [MIT License](http://www.opensource.org/licenses/MIT).
