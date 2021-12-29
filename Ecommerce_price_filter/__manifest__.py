# -*- coding: utf-8 -*-
{
    'name': "Ecommerce Price Filter",


    'description': 'Add filter by price for shop page',

    'author': "Zeinab Elnazeir",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ecommerce',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'website_sale'
    ],

    # always loaded
    'data': [
        'views/assets.xml',
        'views/templates.xml',
    ],

}
