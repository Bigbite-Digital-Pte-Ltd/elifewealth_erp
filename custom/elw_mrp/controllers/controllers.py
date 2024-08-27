import json
from odoo import http
from odoo.http import request

class ManufacturingAPI(http.Controller):


    @http.route('/api/workorder', auth='user', methods=['GET'], csrf=False)
    def list_work_orders(self, **kwargs):
        work_orders = request.env['mrp.workorder'].search([], order='id asc')
        work_orders_data = []
        for work_order in work_orders:
            work_orders_data.append({
                'id': work_order.id,
                'name': work_order.name,
                'state': work_order.state
            })
        return request.make_response(json.dumps({'work_orders': work_orders_data}), headers={'Content-Type': 'application/json'})

    @http.route('/api/workorder/<int:work_order_id>', auth='user', methods=['GET'], csrf=False)
    def find_work_order(self, work_order_id, **kwargs):
        work_order = request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order_data = {
                'id': work_order.id,
                'name': work_order.name,
                'state': work_order.state
            }
            return request.make_response(json.dumps({'work_order': work_order_data}), headers={'Content-Type': 'application/json'})
        else:
            return request.make_response(json.dumps({'error': f'Work order with ID {work_order_id} not found'}), headers={'Content-Type': 'application/json'}, status=404)


    @http.route('/api/workorder/create', auth='user', methods=['POST'], csrf=False)
    def create_work_order(self, **kwargs):
        work_order_name = kwargs.get('name')
        if work_order_name:
            new_work_order = request.env['mrp.workorder'].create({'name': work_order_name})
            return request.make_response(json.dumps({'message': f'Work Order {new_work_order.name} created successfully!'}), headers={'Content-Type': 'application/json'})
        return request.make_response(json.dumps({'error': 'Failed to create Work Order.'}), headers={'Content-Type': 'application/json'}, status=400)

    @http.route('/api/workorder/update/<int:work_order_id>', auth='user', methods=['POST'], csrf=False)
    def update_work_order(self, work_order_id, **kwargs):
        work_order = request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order.write(kwargs)
            return request.make_response(json.dumps({'message': f'Work Order {work_order.name} updated successfully!'}), headers={'Content-Type': 'application/json'})
        return request.make_response(json.dumps({'error': 'Work Order not found.'}), headers={'Content-Type': 'application/json'}, status=404)
    
    @http.route('/api/workorder/delete/<int:work_order_id>', auth='user', methods=['DELETE'], csrf=False)
    def delete_work_order(self, work_order_id, **kwargs):
        work_order = request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order.unlink()
            return request.make_response(json.dumps({'message': f'Work Order {work_order_id} deleted successfully!'}), headers={'Content-Type': 'application/json'})
        return request.make_response(json.dumps({'error': 'Work Order not found.'}), headers={'Content-Type': 'application/json'}, status=404)
