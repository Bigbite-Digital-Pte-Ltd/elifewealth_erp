from odoo import models, fields, api
from datetime import timedelta

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # Additional fields for analysis
    analysis_name = fields.Char(string='Analysis Name')
    quantity_produced = fields.Float(string='Quantity Produced', compute='_compute_quantity_produced', store=True)
    production_date = fields.Date(string='Production Date', default=fields.Date.context_today)
    is_kits = fields.Boolean(string='Is Kit', compute='_compute_is_kits', store=True)
    product_name = fields.Char(string='Product Name', compute='_compute_product_name', store=True)

    @api.depends('product_id')
    def _compute_is_kits(self):
        for record in self:
            bom = self.env['mrp.bom']._bom_find(record.product_id, bom_type='phantom')
            record.is_kits = bool(bom)

    @api.depends('product_id', 'production_date')
    def _compute_quantity_produced(self):
        for record in self:
            if record.product_id and record.production_date:
                date_from = fields.Datetime.to_string(record.production_date - timedelta(days=365))
                domain = [
                    ('state', '=', 'done'),
                    ('product_id', '=', record.product_id.id),
                    ('date_start', '>', date_from)
                ]
                produced = self.env['mrp.production'].read_group(
                    domain, ['product_uom_qty:sum'], ['product_id']
                )
                record.quantity_produced = sum(item['product_uom_qty'] for item in produced) if produced else 0

    # Example of an action method that could be used to analyze production data
    def action_view_production_analysis(self):
        action = self.env.ref('module_name.production_analysis_action').read()[0]
        action['domain'] = [('product_id', 'in', self.mapped('product_id').ids)]
        return action

    @api.depends('product_id')
    def _compute_product_name(self):
        for record in self:
            record.product_name = record.product_id.name if record.product_id else ''
