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
        # Extracting the required fields from the request
        work_order_data = {
            'name': kwargs.get('name'),
            'workcenter_id': kwargs.get('workcenter_id'),
            'product_id': kwargs.get('product_id'),
            'product_uom_id': kwargs.get('product_uom_id'),
            'production_id': kwargs.get('production_id'),
            'duration_percent': kwargs.get('duration_percent'),
            'operation_id': kwargs.get('operation_id'),
            'barcode': kwargs.get('barcode'),
            'production_availability': kwargs.get('production_availability'),
            'state': kwargs.get('state'),
            'qty_produced': kwargs.get('qty_produced'),
            'duration_expected': kwargs.get('duration_expected'),
            'qty_reported_from_previous_wo': kwargs.get('qty_reported_from_previous_wo'),
            'date_start': kwargs.get('date_start'),
            'date_finished': kwargs.get('date_finished'),
            'production_date': kwargs.get('production_date'),
            'duration': kwargs.get('duration'),
            'duration_unit': kwargs.get('duration_unit'),
            'costs_hour': kwargs.get('costs_hour')
        }

        # Remove any keys with None values
        work_order_data = {k: v for k, v in work_order_data.items() if v is not None}

        # Creating the work order
        if work_order_data.get('name'):
            new_work_order = request.env['mrp.workorder'].create(work_order_data)
            return request.make_response(json.dumps({
                'message': f'Work Order {new_work_order.name} created successfully!',
                'work_order_id': new_work_order.id
            }), headers={'Content-Type': 'application/json'})

        return request.make_response(json.dumps({'error': 'Failed to create Work Order.'}),
                                     headers={'Content-Type': 'application/json'}, status=400)

    @http.route('/api/workorder/update/<int:work_order_id>', auth='user', methods=['PUT'], csrf=False)
    def update_work_order(self, work_order_id, **kwargs):
        work_order = request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order.write(kwargs)
            return request.make_response(json.dumps({'message': f'Work Order {work_order.name} updated successfully!'}),
                                         headers={'Content-Type': 'application/json'})
        return request.make_response(json.dumps({'error': 'Work Order not found.'}),
                                     headers={'Content-Type': 'application/json'}, status=404)

    @http.route('/api/workorder/delete/<int:work_order_id>', auth='user', methods=['DELETE'], csrf=False)
    def delete_work_order(self, work_order_id, **kwargs):
        work_order = request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order.unlink()
            return request.make_response(json.dumps({'message': f'Work Order {work_order_id} deleted successfully!'}), headers={'Content-Type': 'application/json'})
        return request.make_response(json.dumps({'error': 'Work Order not found.'}), headers={'Content-Type': 'application/json'}, status=404)
