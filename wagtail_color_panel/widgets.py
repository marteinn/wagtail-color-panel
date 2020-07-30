from django.forms import widgets, Media
from wagtail.admin.staticfiles import versioned_static


class ColorInputWidget(widgets.Input):
    input_type = 'color'

    def __init__(self, attrs=None):
        default_attrs = {"class": "color-input-widget"}
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    # def get_panel(self):
    #     from wagtail_color_panel.edit_handlers import NativeColorPanel
    #     return NativeColorPanel

    @property
    def media(self):
        return Media(css={
            'all': [
                versioned_static('wagtail_color_panel/css/color-input-widget.css'),
            ]
        })
