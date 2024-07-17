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
    maintenance_count = fields.Integer(compute='_compute_maintenance_count', string="Maintenance Count", store=True)
    maintenance_open_count = fields.Integer(compute='_compute_maintenance_count', string="Current Maintenance", store=True)
    maintenance_team_id = fields.Many2one('maintenance.team', string='Maintenance Team', compute='_compute_maintenance_team_id', store=True, readonly=False,
                                      check_company=True)
    technician_user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    effective_date = fields.Date(string='Effective Date')
    expected_mean_time_between_failure = fields.Float(string='Expected Mean Time Between Failure')
    mean_time_between_failure = fields.Float(string='Mean Time Between Failure')
    latest_failure = fields.Date(string='Latest Failure')
    mean_time_to_repair = fields.Float(string='Mean Time To Repair')
    estimated_next_failure = fields.Date(string='Estimated Next Failure')

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


