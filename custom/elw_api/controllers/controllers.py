from odoo import http
from odoo.http import request


class APIController(http.Controller):

    @http.route('/api/partner/create', auth='user', csrf=False)
    def create_partner(self, **kwargs):
        try:
            partner_name = kwargs.get('name')
            email = kwargs.get('email')

            # Create a new partner
            partner = request.env['res.partner'].sudo().create({
                'name': partner_name,
                'email': email,
            })

            return {"status": "success", "partner_id": partner.id}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @http.route('/api/partner/search', auth='user', csrf=False)
    def search_partner(self, **kwargs):
        try:
            domain = [('name', 'ilike', kwargs.get('name', ''))]
            partners = request.env['res.partner'].sudo().search_read(domain, ['name', 'email'])

            return {"status": "success", "partners": partners}
        except Exception as e:
            return {"status": "error", "message": str(e)}
