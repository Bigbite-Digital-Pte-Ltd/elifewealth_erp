from odoo import models, fields, api


class Accounting(models.Model):
    _inherit = 'account.account'

    custom_field = fields.Char(string='Custom Field')

    @api.onchange('custom_field')
    def _onchange_custom_field(self):
        # Custom logic for the field
        if self.custom_field:
            self.name = f'Custom: {self.custom_field}'
