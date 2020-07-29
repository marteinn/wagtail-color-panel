from django.forms import widgets


class ColorInputWidget(widgets.Input):
    input_type = 'color'
