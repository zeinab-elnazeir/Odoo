# -*- coding: utf-8 -*-
import logging
from odoo import http

from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request
from odoo.http import route, request, Controller

_logger = logging.getLogger(__name__)



class MobileZoom(http.Controller):


    @http.route(['/image/zoom/<model("product.template"):product_rec>'], type='http', auth="public", website=True, sitemap=False)
    def pricelist_change(self, product_rec, **post):
        combination_info = product_rec._get_combination_info(only_template=True)

        return request.render('mobile_zoom.zoom_template',{'product':product_rec,'combination_info':combination_info})

