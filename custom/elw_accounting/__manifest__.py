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
        'views/accounting.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
