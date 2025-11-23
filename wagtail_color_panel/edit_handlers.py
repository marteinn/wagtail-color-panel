import warnings

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
    """
    DEPRECATED: This panel uses the Spectrum library for IE11 compatibility.
    Since IE11 is no longer supported by Microsoft (as of June 2022) and this
    package requires Wagtail 6.3+ (which dropped IE11 support), please use
    NativeColorPanel instead.

    This panel will be removed in version 2.0.0.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "PolyfillColorPanel is deprecated and will be removed in "
            "wagtail-color-panel 2.0.0. Use NativeColorPanel instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)

    def get_form_options(self):
        opts = super().get_form_options()
        opts["widgets"] = {
            self.field_name: PolyfillColorInputWidget(),
        }
        return opts
