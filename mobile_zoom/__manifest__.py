# -*- coding: utf-8 -*-
{
    'name': "Website Zoom Product",


    'description': 'Add zoom feature to product image in mobile browsing.',

    'author': "Zeinab Elnazeir",
    'website': "https://github.com/zeinab-elnazeir/Odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'website_sale',
    ],

    # always loaded
    'data': [
        'views/template.xml',
        'views/zoom_template.xml',
        'views/assets.xml',   
    ],

    'images': [
        'static/description/Screenshot.png',
     
    ],

}
