![Wagtail-Color-Panel](https://github.com/marteinn/wagtail-color-panel/workflows/Wagtail-Color-Panel/badge.svg)

# Wagtail-Color-Panel

Introduces a color field and panel to Wagtail.


## Features

- Color panel that uses the HTML5 input color
- A custom db field called ColorField


## Examples

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


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-Color-Panel is released under the [MIT License](http://www.opensource.org/licenses/MIT).
