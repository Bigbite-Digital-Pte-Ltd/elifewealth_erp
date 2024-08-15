{
    'name': 'ELW Accounting',
    'version': '1.0',
    'summary': 'Custom Accounting Module',
    'description': 'A module to manage custom accounting features.',
    'category': 'ELW',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'sequence': -100,
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/accounting_views.xml',
        'views/accounting_actions.xml',
        'views/accounting_menus.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
