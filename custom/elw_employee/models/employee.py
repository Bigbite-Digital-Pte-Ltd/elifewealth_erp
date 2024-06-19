from odoo import models, fields

class Employee(models.Model):
    _name = 'custom.employee'
    _description = 'Custom Employee Model'

    name = fields.Char(string='Name', required=True)
    work_email = fields.Char(string='Work Email')
    work_phone = fields.Char(string='Work Phone')
    work_mobile = fields.Char(string='Work Mobile')
    department = fields.Many2one('hr.department', string='Department')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    notes = fields.Text(string='Notes')
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status')
    date_of_birth = fields.Date(string='Date of Birth')
    nationality = fields.Char(string='Nationality (Country)')
    identification_no = fields.Char(string='Identification No')
    passport_no = fields.Char(string='Passport No')
    visa_no = fields.Char(string='Visa No')
    work_permit_no = fields.Char(string='Work Permit No')
    visa_expire_date = fields.Date(string='Visa Expire Date')
    image = fields.Binary(string='Image')
