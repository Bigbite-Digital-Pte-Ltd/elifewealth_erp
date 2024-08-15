from odoo import models, fields

class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    uom_id = fields.Many2one('uom.uom', string="Unit of Measurement")
