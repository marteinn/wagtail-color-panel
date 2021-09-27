(function() {
    function ColorInput(html) {
        this.html = html;
    }
    ColorInput.prototype.render = function(placeholder, name, id, initialState) {
        var html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        placeholder.outerHTML = html;

        var colorInput = new ColorInputWidget(id);
        colorInput.setState(initialState);
        return colorInput;
    };

    window.telepath.register('wagtail_color_panel.widgets.ColorInput', ColorInput);
})();
