function ColorInputWidget(id) {
    /*
    id = the ID of the HTML element where color input behaviour should be attached
    */
    this.textInput = $('#' + id);
    this.colorInput = $('#' + id + '-color');

    this.textInput.on('input', this.handleUpdate.bind(this));
    this.colorInput.on('input', this.handleUpdate.bind(this));
}

ColorInputWidget.prototype.handleUpdate = function(evt) {
    this.setState(evt.target.value);
};

ColorInputWidget.prototype.setState = function(newState) {
    this.textInput.val(newState);
    this.colorInput.val(newState);
};

ColorInputWidget.prototype.getState = function() {
    return this.textInput.val();
};

ColorInputWidget.prototype.getValue = function() {
    return this.textInput.val();
};

ColorInputWidget.prototype.focus = function() {
    this.textInput.focus();
}
