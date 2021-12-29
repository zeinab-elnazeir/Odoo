# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
_logger = logging.getLogger(__name__)

#
#


class WebsiteSale(WebsiteSale):


    def sitemap_shop(env, rule, qs):
        if not qs or qs.lower() in '/shop':
            yield {'loc': '/shop'}

        Category = env['product.public.category']
        dom = sitemap_qs2dom(qs, '/shop/category', Category._rec_name)
        dom += env['website'].get_current_website().website_domain()
        for cat in Category.search(dom):
            loc = '/shop/category/%s' % slug(cat)
            if not qs or qs.lower() in loc:
                yield {'loc': loc}

    
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=sitemap_shop)
    def shop(self, page=0, category=None, search='',min_price=0.0, max_price=0.0, ppg=False, **post):
        response = super(WebsiteSale,self).shop(page=page, category=category, search=search, ppg=ppg, **post)

        try:
            min_price = float(min_price)
        except ValueError:
            min_price = 0
        try:
            max_price = float(max_price)
        except ValueError:
            max_price = 0

        Product = request.env['product.template'].with_context(bin_size=True)
        company_currency = request.website.company_id.currency_id
        pricelist_context, pricelist = self._get_pricelist_context()
        conversion_rate = request.env['res.currency']._get_conversion_rate(company_currency, pricelist.currency_id, request.website.company_id, fields.Date.today())

        domain = self._get_search_domain(search, category, response.qcontext['attrib_values'])

        # This is ~4 times more efficient than a search for the cheapest and most expensive products
        from_clause, where_clause, where_params = Product._where_calc(domain).get_sql()
        query = f"""
            SELECT COALESCE(MIN(list_price), 0) * {conversion_rate}, COALESCE(MAX(list_price), 0) * {conversion_rate}
              FROM {from_clause}
             WHERE {where_clause}
        """
        request.env.cr.execute(query, where_params)
        available_min_price, available_max_price = request.env.cr.fetchone()

        min_price = min_price if min_price <= available_max_price else available_min_price
        post['min_price'] = min_price
        max_price = max_price if max_price >= available_min_price else available_max_price
        post['max_price'] = max_price

        products = response.qcontext['products'].sudo().filtered(lambda l: min_price <= l.list_price <= max_price)
        response.qcontext.update({
                'available_min_price':tools.float_round(available_min_price, 2),
                'available_max_price':tools.float_round(available_max_price, 2),
                'min_price':min_price or available_min_price,
                'max_price':max_price or available_max_price,
                'products':products,
                'bins': TableCompute().process(products, response.qcontext['ppg'], response.qcontext['ppr']),
                })

        return response
