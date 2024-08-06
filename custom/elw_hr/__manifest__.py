{
    'name': 'ELW HR',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Custom HR module for Odoo',
    'description': """
        A custom HR module to manage employee records and additional features.
    """,
    'sequence': -100,
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': True,
}
