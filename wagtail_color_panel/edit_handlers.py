from wagtail.admin.panels import FieldPanel

from wagtail_color_panel.widgets import ColorInputWidget, PolyfillColorInputWidget


class NativeColorPanel(FieldPanel):
    def get_form_options(self):
        opts = super().get_form_options()
        opts["widgets"] = {
            self.field_name: ColorInputWidget(),
        }
        return opts


class PolyfillColorPanel(FieldPanel):
    def get_form_options(self):
        opts = super().get_form_options()
        opts["widgets"] = {
            self.field_name: PolyfillColorInputWidget(),
        }
        return opts
