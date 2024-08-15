from odoo import http


class ManufacturingAPI(http.Controller):
    @http.route('/api/print', auth='public')
    def print_message(self, **kwargs):
        sales_order = http.request.env['sale.order'].search([])
        output = "<h1>Sales Orders:<h1><u1>"
        for sale in sales_order:
            output+= '<li>' + sale['name'] + '</li>'
        output+= "</ul>"
        return output
