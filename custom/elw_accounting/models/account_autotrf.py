from odoo import models, fields


class AccountAutoTrf(models.Model):
    _name = 'account.autotrf'
    _description = 'Automatic Transfers'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    stop_date = fields.Date(string='Stop Date')
    frequency = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ], string='Frequency', default='monthly')
