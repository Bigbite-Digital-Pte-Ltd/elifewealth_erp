from odoo import models, fields

class Employee(models.Model):
    _name = 'custom.employee'
    _description = 'Custom Employee Model'

    name = fields.Char(string='Name', required=True)
    job_title = fields.Char(string='Job Title')
    department = fields.Many2one('hr.department', string='Department')
    email = fields.Char(string='Email')
