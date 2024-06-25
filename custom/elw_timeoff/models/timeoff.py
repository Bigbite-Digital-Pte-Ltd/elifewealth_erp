from odoo import models, fields

class CustomTimeOff(models.Model):
    _name = 'custom.timeoff'
    _description = 'Custom Time Off'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    type = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], string='Type', default='paid')
    date_from = fields.Date(string='From', required=True)
    date_to = fields.Date(string='To', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('validate', 'Validated'),
        ('approve', 'Approved'),
        ('refuse', 'Refused'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    notes = fields.Text(string='Notes')
    manager_id = fields.Many2one('hr.employee', string='Manager')

    # Override methods if needed
    def action_approve(self):
        # Custom logic here
        return super(CustomTimeOff, self).action_approve()
