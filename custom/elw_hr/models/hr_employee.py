from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Add new fields
    custom_field_1 = fields.Char(string='Custom Field 1')
    custom_field_2 = fields.Date(string='Custom Field 2')
