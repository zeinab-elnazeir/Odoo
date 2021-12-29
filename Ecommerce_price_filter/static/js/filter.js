odoo.define('website_sale.price_range_option', function (require) {
'use strict';

const publicWidget = require('web.public.widget');

publicWidget.registry.multirangePriceSelector = publicWidget.Widget.extend({
    selector: '#o_wsale_price_range_option',
    events: {
        'newRangeValue input[type="range"]': '_onPriceRangeSelected',
    },

    //----------------------------------------------------------------------
    // Handlers
    //----------------------------------------------------------------------

    /**
     * @private
     * @param {Event} ev
     */
    _onPriceRangeSelected(ev) {
        const range = ev.currentTarget;
        const search = $.deparam(window.location.search.substring(1));
        delete search.min_price;
        delete search.max_price;
        if (parseFloat(range.min) !== range.valueLow) {
            search['min_price'] = range.valueLow;
        }
        if (parseFloat(range.max) !== range.valueHigh) {
            search['max_price'] = range.valueHigh;
        }
        window.location.search = $.param(search);
    },
});
});