from django.forms import widgets, Media
from django.utils.safestring import mark_safe
from wagtail.admin.staticfiles import versioned_static


class PolyfillColorInputWidget(widgets.TextInput):
    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/spectrum/1.8.0/spectrum.min.css",
            )
        }

        js = ("https://cdnjs.cloudflare.com/ajax/libs/spectrum/1.8.0/spectrum.min.js",)

    def render(self, name, value, attrs=None, renderer=None):
        out = super().render(name, value, attrs, renderer=renderer)
        field_id = attrs["id"]

        return mark_safe(
            out
            + """
            <script>
            (function(){
                function init() {
                    $("#__FIELD_ID__").spectrum({
                        showPalette: false,
                        preferredFormat: "hex",
                        showInput: true,
                    });
                }

                if (document.readyState === 'complete') {
                    init({});
                }

                $(window).on('load', function() {
                    init();
                });
            })();
            </script>
            """.replace(
                "__FIELD_ID__", field_id
            )
        )


class ColorInputWidget(widgets.TextInput):
    template_name = "wagtail_color_panel/widgets/color-input-widget.html"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "color-input-widget__text-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    @property
    def media(self):
        return Media(
            css={
                "all": [
                    versioned_static("wagtail_color_panel/css/color-input-widget.css"),
                ]
            }
        )
