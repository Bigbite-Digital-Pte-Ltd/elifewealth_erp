import requests
from odoo import http

class ManufacturingAPI(http.Controller):

    # READ: List all work orders
    @http.route('/api/workorder', auth='user')
    def list_work_orders(self, **kwargs):
        work_orders = http.request.env['mrp.workorder'].search([], order='id asc')
        output = "<h1>Work Orders:</h1><ul>"
        for work_order in work_orders:
            output += f'<li>{work_order.id} | {work_order.name} | {work_order.state}</li>'
        output += "</ul>"

        return output


    # CREATE: Create a new work order
    @http.route('/api/workorder/create', auth='user', methods=['POST'], csrf=False)
    def create_work_order(self, **kwargs):
        work_order_name = kwargs.get('name')
        if work_order_name:
            new_work_order = http.request.env['mrp.workorder'].create({'name': work_order_name})
            return f'Work Order {new_work_order.name} created successfully!'
        return 'Failed to create Work Order.'


    # UPDATE: Update an existing work order
    @http.route('/api/workorder/update/<int:work_order_id>', auth='user', methods=['POST'], csrf=False)
    def update_work_order(self, work_order_id, **kwargs):
        work_order = http.request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order.write(kwargs)
            return f'Work Order {work_order.name} updated successfully!'
        return 'Work Order not found.'


    # DELETE: Delete a work order
    @http.route('/api/workorder/delete/<int:work_order_id>', auth='user', methods=['POST'], csrf=False)
    def delete_work_order(self, work_order_id, **kwargs):
        work_order = http.request.env['mrp.workorder'].browse(work_order_id)
        if work_order.exists():
            work_order.unlink()
            return f'Work Order {work_order_id} deleted successfully!'
        return 'Work Order not found.'


# class IMES_API(http.Controller):
#     @http.route('/api/fetch_backend', auth='public')
#     def fetch_data_from_localhost(self, **kwargs):
#         url = ''
#
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             data = response.json()
#
#             output = f"<h1>Data from localhost service:</h1><pre>{data}</pre>"
#             return output
#         except requests.exceptions.RequestException as e:
#             return f"<h1>Error communicating with the localhost service:</h1><p>{str(e)}</p>"
#
#         @http.route('/api/send_backend', auth='public')
#         def send_data_from_localhost(self, **kwargs):
#             url = ''