
odoo.define('mobile_zoom.mobileZoom', function (require) {
    "use strict";

    require('web.dom_ready');
    var config = require('web.config');
    var ajax = require('web.ajax');


    if(!$('.oe_website_sale').length) {
        return $.Deferred().reject("DOM doesn't contain '.oe_website_sale'");
    }
    $('.oe_website_sale').each(function () {
        var oe_website_sale = this;

        if ($(".carousel-inner").length) {
                   $(oe_website_sale).on('click', "div[id='MobileZoom']", function () {
                    if (config.device.isMobile) {
                        var url = '/image/zoom/' + $("#zoom_product_id").val()
                         window.open(url);              
                    }
                    });

                }
    });
    });
