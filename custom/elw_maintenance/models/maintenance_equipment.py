from odoo import api, fields, models

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    name = fields.Char(string='Equipment Name', required=True)
    technician_user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    category_id = fields.Many2one('equipment.category', string='Category', required=True)
    mean_time_between_failure = fields.Float(string='Mean Time Between Failures')
    mean_time_to_repair = fields.Float(string='Mean Time To Repair')
    estimated_next_failure = fields.Date(string='Estimated Next Failure')
