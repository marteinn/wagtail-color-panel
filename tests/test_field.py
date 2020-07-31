from django.test import TestCase
from django.core.exceptions import ValidationError
from wagtail.tests.utils import WagtailTestUtils

from tests.testapp.factories import (
    PageWithColorFieldPageFactory,
    PageWithDefaultValuePageFactory,
)


class FieldTest(TestCase, WagtailTestUtils):
    def test_strings_larger_than_7_raises_error(self):
        with self.assertRaises(ValidationError) as _ctx:
            PageWithColorFieldPageFactory.create(color="#000000E")

    def test_value_not_beginning_with_hash_raises_error(self):
        with self.assertRaises(ValidationError) as ctx:
            PageWithColorFieldPageFactory.create(color="_000000")
        self.assertTrue("Enter a valid color hash" in str(ctx.exception))

    def test_invalid_color_hash_value_raises_error(self):
        with self.assertRaises(ValidationError) as ctx:
            PageWithColorFieldPageFactory.create(color="#0G0000")
        self.assertTrue("Enter a valid color hash" in str(ctx.exception))

    def test_valid_value_are_saved_and_treated_as_a_string(self):
        page = PageWithColorFieldPageFactory.create(color="#FF0000")
        self.assertEqual(page.color, "#FF0000")

    def test_field_gets_default_value(self):
        page = PageWithDefaultValuePageFactory.create()
        self.assertEqual(page.color, "#FF0000")
