// wagtail_color_panel/static/wagtail_color_panel/js/color-input-controller.js

class ColorInputController extends window.StimulusModule.Controller {
    connect() {
        new ColorInputWidget(this.element.id);
    }
}

window.wagtail.app.register('color-input', ColorInputController);
