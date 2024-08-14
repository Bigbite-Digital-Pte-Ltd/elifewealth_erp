# -*- coding: utf-8 -*-
{
    'name': "ELW ERP",

    'summary': "ELW ERP Management",

    'description': """
Long description of module's purpose
    """,
    'application': True,
    'sequence': -150,
    'author': "Digital BigBite",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ELW',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends':
        ['elw_maintenance',
        'elw_inventory',
        'elw_quality',
        'elw_accounting',
         'elw_hr',
        'sale_management',
        'pos_restaurant',
        'account',
        'crm',
        'website',
        'stock',
        'purchase',
        'point_of_sale',
        'project',
        'website_sale',
        'mrp',
        'mass_mailing',
        'hr_expense',
        'hr_holidays',
        'hr_recruitment',
        'hr',
        'data_recycle',
        'maintenance',
        'website_slides',
        'website_event',
        'mail',
        'contacts',
        'calendar',
        'fleet',
        'im_livechat',
        'survey',
        'repair',
        'hr_attendance',
        'mass_mailing_sms',
        'project_todo',
        'hr_skills',
        'lunch',
        'website_hr_recruitment',
        'hr_contract'],

    # always loaded
    'data': [
        'security/elw_module_security_data.xml',
        # 'security/ir.model.access.csv',
        'views/ir_module_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': True,
}
