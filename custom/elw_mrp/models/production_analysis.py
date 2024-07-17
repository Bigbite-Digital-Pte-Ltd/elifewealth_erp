from odoo import models, fields, api

class ProductionAnalysis(models.Model):
    _name = 'production.analysis'
    _description = 'Production Analysis'

    # Define fields
    name = fields.Char(string='Analysis Name')
    product_id = fields.Many2one('product.product', string='Product')
    quantity_produced = fields.Float(string='Quantity Produced')
    production_date = fields.Date(string='Production Date')