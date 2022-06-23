from wagtail import VERSION as WAGTAIL_VERSION

from wagtail_color_panel.widgets import ColorInputWidget, PolyfillColorInputWidget

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import FieldPanel
else:
    from wagtail.admin.edit_handlers import FieldPanel


class NativeColorPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: ColorInputWidget(),
        }


class PolyfillColorPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: PolyfillColorInputWidget(),
        }
