from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils

# from wagtail.admin.edit_handlers import get_form_for_model
# from wagtail.admin.forms import WagtailAdminModelForm, WagtailAdminPageForm

from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.widgets import ColorInputWidget
from tests.testapp.factories import PageWithColorFieldPageFactory
from tests.testapp.models import PageWithColorField


class PanelTest(TestCase, WagtailTestUtils):
    def test_field_to_panel_mapping(self):
        """
        PageWithColorFieldPageForm = get_form_for_model(
            PageWithColorField,
            form_class=WagtailAdminPageForm
        )
        form = PageWithColorFieldPageForm()
        """

    def test_native_color_panel_uses_correct_widget(self):
        page = PageWithColorFieldPageFactory.create(color="#000000")

        color_panel = page.content_panels[1]
        self.assertEqual(color_panel.__class__, NativeColorPanel)

        color_widget = color_panel.widget_overrides()["color"]
        self.assertEqual(color_widget.__class__, ColorInputWidget)
