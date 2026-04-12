from django.test import TestCase
from wagtail.test.utils import WagtailTestUtils

from tests.testapp.factories import PageWithColorFieldPageFactory
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.widgets import ColorInputWidget, PolyfillColorInputWidget


class PanelTest(TestCase, WagtailTestUtils):
    def test_native_color_panel_uses_correct_widget(self):
        page = PageWithColorFieldPageFactory.create(color="#000000")

        color_panel = page.content_panels[1]
        self.assertEqual(color_panel.__class__, NativeColorPanel)

        # Bind the panel to the model before calling get_form_options
        bound_panel = color_panel.bind_to_model(page.__class__)
        color_widget = bound_panel.get_form_options()["widgets"]["color"]
        self.assertEqual(color_widget.__class__, ColorInputWidget)


class PolyfillWidgetTest(TestCase, WagtailTestUtils):
    def test_polyfill_widget_escapes_field_id_with_special_chars(self):
        """Test that field IDs with quotes are properly escaped in JavaScript"""
        widget = PolyfillColorInputWidget()

        # Test with field ID containing quotes
        html = widget.render(
            name="color",
            value="#FF0000",
            attrs={"id": 'my"field'},
        )

        # Should contain properly escaped JavaScript string with # prefix
        self.assertIn(r'$("#" + "my\"field")', html)
        # Should not contain unescaped quote that would break JavaScript
        self.assertNotIn('$("#" + "my"field")', html)
