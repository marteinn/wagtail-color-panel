from wagtail.admin.edit_handlers import FieldPanel

from wagtail_color_panel.widgets import ColorInputWidget


class NativeColorPanel(FieldPanel):
    def widget_overrides(self):
        return {
            self.field_name: ColorInputWidget(),
        }

