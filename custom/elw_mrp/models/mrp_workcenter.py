from typing import Dict, List

from odoo import models, fields, api, SUPERUSER_ID, _
import logging
_logger = logging.getLogger(__name__)

class MrpWorkcenter(models.Model):
    _name = 'mrp.workcenter'
    _inherit = ['mrp.workcenter', 'mail.thread', 'mail.activity.mixin']

    equipment_ids = fields.One2many('maintenance.equipment', 'workcenter_id', string='Equipment', store=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    maintenance_ids = fields.One2many('maintenance.request', 'workcenter_id', string='Maintenance', store=True)
    maintenance_count = fields.Integer(compute='_compute_maintenance_count', string="Maintenance Count", store=True, group_operator=False)
    maintenance_open_count = fields.Integer(compute='_compute_maintenance_count', string="Current Maintenance", store=True, group_operator=False)
    maintenance_team_id = fields.Many2one('maintenance.team', string='Maintenance Team', compute='_compute_maintenance_team_id', store=True, readonly=False,
                                          check_company=True)
    technician_user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    effective_date = fields.Date(string='Effective Date')
    expected_mean_time_between_failure = fields.Float(string='Expected Mean Time Between Failure', group_operator=False)
    latest_failure = fields.Date(string='Latest Failure')
    estimated_next_failure = fields.Date(string='Estimated Next Failure')
    mean_time_between_failure = fields.Float(string='Mean Time Between Failure')
    mean_time_to_repair = fields.Float(string='Mean Time To Repair', group_operator=False)
    expected_duration = fields.Float(string='Expected Duration')
    duration_per_unit = fields.Float(string='Duration Per Unit')
    duration_minutes = fields.Float(string='Duration (minutes)')

    carried_quantity = fields.Float(string='Carried Quantity', compute='_compute_carried_quantity', store=True)
    cost_per_hour = fields.Float(string='Cost per Hour', compute='_compute_cost_per_hour', store=True)
    duration_deviation_percentage = fields.Float(string='Duration Deviation (%)',
                                                 compute='_compute_duration_deviation_percentage', store=True)
    quantity = fields.Float(string='Quantity', compute='_compute_quantity', store=True)
    count = fields.Integer(string='Count', compute='_compute_count', store=True)

    @api.depends('expected_duration')
    def _compute_duration_minutes(self):
        for record in self:
            record.duration_minutes = record.expected_duration * 60

    @api.depends('expected_duration', 'quantity')
    def _compute_duration_per_unit(self):
        for record in self:
            if record.quantity > 0:
                record.duration_per_unit = record.expected_duration / record.quantity
            else:
                record.duration_per_unit = 0.0

    @api.depends('expected_duration', 'duration_minutes')
    def _compute_duration_deviation_percentage(self):
        for record in self:
            if record.expected_duration:
                record.duration_deviation_percentage = ((record.duration_minutes - record.expected_duration * 60) / (record.expected_duration * 60)) * 100
            else:
                record.duration_deviation_percentage = 0

    @api.depends('maintenance_ids')
    def _compute_carried_quantity(self):
        for record in self:
            record.carried_quantity = sum(maintenance.requested_qty for maintenance in record.maintenance_ids)

    @api.depends('duration_minutes', 'maintenance_ids')
    def _compute_cost_per_hour(self):
        for record in self:
            total_cost = sum(maintenance.cost for maintenance in record.maintenance_ids)
            if record.duration_minutes > 0:
                record.cost_per_hour = total_cost / (record.duration_minutes / 60)
            else:
                record.cost_per_hour = 0.0

    @api.depends('maintenance_ids')
    def _compute_quantity(self):
        for record in self:
            record.quantity = sum(maintenance.qty_done for maintenance in record.maintenance_ids)

    @api.depends('maintenance_ids')
    def _compute_count(self):
        for record in self:
            record.count = len(record.maintenance_ids)

    @api.depends('company_id')
    def _compute_maintenance_team_id(self):
        for record in self:
            if record.maintenance_team_id.company_id and record.maintenance_team_id.company_id.id != record.company_id.id:
                record.maintenance_team_id = False

    @api.depends('maintenance_ids.stage_id.done', 'maintenance_ids.archive')
    def _compute_maintenance_count(self):
        for record in self:
            record.maintenance_count = len(record.maintenance_ids)
            record.maintenance_open_count = len(record.maintenance_ids.filtered(lambda mr: not mr.stage_id.done and not mr.archive))

    @api.onchange('equipment_ids')
    def onchange_equipment_ids(self):
        for eq_obj in self.equipment_ids:
            eq_obj.write({'workcenter_id': self._origin.id})
