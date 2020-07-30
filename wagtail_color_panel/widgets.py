from django.forms import widgets


class ColorInputWidget(widgets.Input):
    input_type = 'color'

    # def get_panel(self):
    #     from wagtail_color_panel.edit_handlers import NativeColorPanel
    #     return NativeColorPanel
