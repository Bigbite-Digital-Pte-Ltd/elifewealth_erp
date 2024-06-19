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
    'category': 'ELW/ELW Employee',
    'version': '0.1',
    'depends': [
        'base', 'hr',
    ],
    'data': [
        'views/employee_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
