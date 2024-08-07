{
    'name': 'ELW Accounting',
    'version': '1.0',
    'summary': 'Custom Accounting Module',
    'description': 'A module to manage custom accounting features.',
    'category': 'ELW/ELW Accounting',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'sequence': -100,
    'depends': ['base', 'account'],
    'data': [
        'views/accounting.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
