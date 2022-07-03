from wagtail import VERSION as WAGTAIL_VERSION

from wagtail_color_panel.widgets import ColorInputWidget, PolyfillColorInputWidget

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import FieldPanel
else:
    from wagtail.admin.edit_handlers import FieldPanel


class NativeColorPanel(FieldPanel):
    def widget_overrides(self):
        # For Wagtail<3.0 we use widget_overrides
        return {
            self.field_name: ColorInputWidget(),
        }

    def get_form_options(self):
        # For Wagtail 3.0 we use get_form_options
        # So we can mix them to provide supports to Wagtail 2,3
        opts = super().get_form_options()
        opts["widgets"] = self.widget_overrides()
        return opts


class PolyfillColorPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: PolyfillColorInputWidget(),
        }

    def get_form_options(self):
        opts = super().get_form_options()
        opts["widgets"] = self.widget_overrides()
        return opts
