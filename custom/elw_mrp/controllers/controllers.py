from odoo import http
from odoo.http import request, Response
import json


class ManufacturingAPI(http.Controller):
    @http.route('/api/print', type='http', auth='user', methods=['GET', 'POST'], csrf=False)
    def print_message(self, **kwargs):
            # Extract message, username, and password from request parameters
            username = kwargs.get('username', 'default_user')
            password = kwargs.get('password', 'default_pass')

            # Create the response dictionary
            response_data = {
                'username': username,
                'password': password
            }

            # Convert the dictionary to a JSON string
            response_json = json.dumps(response_data)

            # Return the response as a JSON object
            return Response(response_json, content_type='application/json;charset=utf-8')
