# -*- coding: utf-8 -*-
{
    'name': "ELW Time Off",
    'summary': "ELW Time Off",
    'description': """
Long description of module's purpose
    """,
    'application': True,
    'sequence': -115,
    'author': "Digital BigBite",
    'website': "https://www.yourcompany.com",
    'category': 'ELW/ELW Time Off',
    'version': '0.1',
    'depends': [
        'base', 'hr'
    ],
    'data': [
        'views/timeoff_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
