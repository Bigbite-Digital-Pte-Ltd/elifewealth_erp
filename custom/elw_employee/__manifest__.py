# -*- coding: utf-8 -*-
{
    'name': "ELW Employee",

    'summary': "ELW Employee",

    'description': """
Long description of module's purpose
    """,
    'application': True,
    'sequence': -115,
    'author': "Digital BigBite",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ELW/ELW Employee',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        #'base', 'product', 'stock', 'purchase', 'sale'
        ],

    # always loaded
    'data': [
        'views/employee_views.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    # 'installable': True,
    # 'auto_install': True,
}
