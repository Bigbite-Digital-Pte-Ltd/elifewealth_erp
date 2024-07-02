from odoo import models, fields, api

class CustomEmployee(models.Model):
    _name = 'custom.employee'
    _inherit = ['hr.employee.base']

    parent_id = fields.Many2one('res.partner', string='Parent')
    child_ids = fields.One2many('custom.employee.child', 'parent_id', string='Children')
    child_all_count = fields.Integer(string='Number of Children', compute='_compute_subordinates')

    @api.depends('child_ids')
    def _compute_subordinates(self):
        for record in self:
            record.child_all_count = len(record.child_ids)
