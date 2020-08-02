from django.core.exceptions import ValidationError
from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils

from wagtail_color_panel.blocks import NativeColorBlock


class BlockTest(TestCase, WagtailTestUtils):
    def test_color_block_render(self):
        block = NativeColorBlock()
        html = block.render("#333333")

        self.assertEqual("#333333", html)

    def test_form_uses_proper_input_type(self):
        block = NativeColorBlock()
        html = block.render_form("#333333")

        self.assertIn('type="color"', html)

    def test_that_hex_colors_are_validated(self):
        block = NativeColorBlock()
        with self.assertRaises(ValidationError) as ctx:
            block.clean("Invalid")

        self.assertTrue("Enter a valid color hash" in str(ctx.exception))

    def test_color_block_supports_default_value(self):
        default_value = NativeColorBlock(default="#333333").get_default()
        self.assertEqual("#333333", default_value)
