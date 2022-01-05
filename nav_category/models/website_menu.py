# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    category_check = fields.Boolean("Category Check")

    def compute_mega_content(self):
        link_str = ""
        categories = self.env['product.public.category'].sudo().search([('parent_id', '=', False)])

        for rec in self:
            if rec.category_check:
                for category in categories:
                    
                    link_str += """<div class="col-md-3 text-center"><nav class="nav flex-column mx-auto"><h5 class="border-nav o_default_snippet_text"><a href="/shop/category/"""+ str(category.id)+"""" class="nav-link mega-link o_default_snippet_text font-weight-bold" data-name="Menu Item">"""+category.name+"""</a></h5></br>"""
                    
                    if category.child_id:
                        for c in category.child_id:
                            link_str += """<li><a href="/shop/category/"""+ str(c.id)+"""" class="nav-link  d-flex d-block o_default_snippet_text" data-name="Menu Item">"""+c.name+"""</a></li>"""

                    link_str+= '</nav></div>'

                templates = '''<section class="s_mega_menu_menu_image_menu py-4">
                        <div class="container">
                            <div class="row align-items-center">
                             <div class='col-12 row'>''' + link_str+''' </div></div></div></section>'''

                rec.sudo().update({'mega_menu_content':templates})
                return templates