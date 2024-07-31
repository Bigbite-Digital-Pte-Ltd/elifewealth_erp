from odoo import models, fields, api
from datetime import timedelta

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # Additional fields for analysis
    analysis_name = fields.Char(string='Analysis Name')
    quantity_produced = fields.Float(string='Quantity Produced', compute='_compute_quantity_produced', store=True)
    production_date = fields.Date(string='Production Date', default=fields.Date.context_today)
    product_name = fields.Char(string='Product Name', compute='_compute_product_name', store=True)
    total_cost = fields.Float(string='Total Cost', compute='_compute_costs', store=True)
    cost_per_unit = fields.Float(string='Cost / Unit', compute='_compute_cost_per_unit', store=True)
    duration_minutes = fields.Float(string='Duration (minutes)', compute='_compute_duration_minutes', store=True)
    duration_per_unit = fields.Float(string='Duration Per Unit', compute='_compute_duration_per_unit', store=True)
    expected_duration = fields.Float(
        string='Expected Duration',
        compute='_compute_expected_duration',
        store=True
    )

    @api.depends('production_id.workorder_ids')  # Compute based on related work orders
    def _compute_expected_duration(self):
        for record in self:
            if record.production_id:
                # Sum of expected durations for all related work orders
                total_duration = sum(workorder.duration_expected for workorder in record.production_id.workorder_ids)
                record.expected_duration = total_duration
            else:
                record.expected_duration = 0.0

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

    @api.depends('product_id')
    def _compute_product_name(self):
        for record in self:
            record.product_name = record.product_id.name if record.product_id else ''

    @api.depends('move_raw_ids')
    def _compute_costs(self):
        for production in self:
            # Calculate total cost
            total_cost = sum(move.price_unit * move.product_uom_qty for move in production.move_raw_ids)
            production.total_cost = total_cost

    @api.depends('product_qty', 'total_cost')
    def _compute_cost_per_unit(self):
        for record in self:
            if record.product_qty > 0:
                record.cost_per_unit = record.total_cost / record.product_qty
            else:
                record.cost_per_unit = 0.0

    @api.depends('expected_duration')
    def _compute_duration_minutes(self):
        for record in self:
            record.duration_minutes = record.expected_duration * 60

    @api.depends('expected_duration', 'product_qty')
    def _compute_duration_per_unit(self):
        for record in self:
            if record.product_qty > 0:
                record.duration_per_unit = record.expected_duration / record.product_qty
            else:
                record.duration_per_unit = 0.0

    def action_view_production_analysis(self):
        action = self.env.ref('module_name.production_analysis_action').read()[0]
        action['domain'] = [('product_id', 'in', self.mapped('product_id').ids)]
        return action
