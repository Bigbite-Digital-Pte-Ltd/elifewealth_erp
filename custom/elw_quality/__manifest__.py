# -*- coding: utf-8 -*-
{
    'name': "ELW Quality",

    'summary': "Quality control",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'sequence': -120,
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ELW',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'data/quality_test_type_data.xml',
        'views/quality_point_view.xml',
        'views/quality_check_view.xml',
        'views/product_view.xml',
        'views/configuration_view.xml',
        'views/quality_test_type.xml',
        'views/quality_menu.xml',
    ],
    # only loaded in demonstration mode

    'license': 'LGPL-3',
}
