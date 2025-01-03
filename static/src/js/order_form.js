odoo.define('portal_order_management.order_form', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.OrderFormWidget = publicWidget.Widget.extend({
        selector: '.container', // Ensure this selector is always available
        events: {
            'click #add-line-btn': '_onAddLineClick',
            'click .remove-line': '_onRemoveLineClick',
        },

        // Triggered when "Add Line" is clicked
        _onAddLineClick: function (ev) {
            console.log("Add Line button clicked"); // Debug log
            var lineTemplate = `
                <div class="order-line row mb-3">
                    <div class="col-md-4">
                        <label for="product_id">Product</label>
                        <select name="product_id[]" class="form-control" required="1">
                            ${$('#order-lines-container .order-line select[name="product_id[]"]').html()}
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label for="qty">Quantity</label>
                        <input type="number" name="qty[]" class="form-control" required="1" min="1" value="1"/>
                    </div>
                    <div class="col-md-2">
                        <label for="price_unit">Price Unit</label>
                        <input type="number" name="price_unit[]" class="form-control" required="1" min="0.01" step="0.01" value="0.01"/>
                    </div>
                    <div class="col-md-2 d-flex align-items-end">
                        <button type="button" class="btn btn-danger remove-line">Remove</button>
                    </div>
                </div>
            `;
            $('#order-lines-container').append(lineTemplate);
        },

        // Triggered when "Remove Line" is clicked
        _onRemoveLineClick: function (ev) {
            $(ev.currentTarget).closest('.order-line').remove();
        },
    });
});
