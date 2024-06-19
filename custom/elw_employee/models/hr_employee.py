import xlrd
from odoo import models, api

class ImportHrEmployee(models.Model):
    _name = 'import.employee'  # Adjust if needed

    @api.model
    def import_hr_employee_data(self):
        file_path = 'static/xls/hr_employee.xls'  # Adjust path as per your module structure
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_index(0)  # Assuming data is in the first sheet

        Employee = self.env['custom.employee']

        for row in range(1, sheet.nrows):  # Start from row 1 to skip header
            name = sheet.cell_value(row, 0)
            work_email = sheet.cell_value(row, 1)
            work_phone = sheet.cell_value(row, 2)
            work_mobile = sheet.cell_value(row, 3)
            department_name = sheet.cell_value(row, 4)  # Assuming department name is in column 5 (index 4)

            # Find or create department based on name
            department = self.env['hr.department'].search([('name', '=', department_name)], limit=1)
            if not department:
                department = self.env['hr.department'].create({'name': department_name})

            # Prepare employee values
            employee_vals = {
                'name': name,
                'work_email': work_email,
                'work_phone': work_phone,
                'work_mobile': work_mobile,
                'department': department.id,  # Use department.id instead of department
                'gender': sheet.cell_value(row, 5),  # Assuming gender is in column 6 (index 5)
                'notes': sheet.cell_value(row, 6),  # Assuming notes is in column 7 (index 6)
                'marital_status': sheet.cell_value(row, 7),  # Assuming marital status is in column 8 (index 7)
                'date_of_birth': xlrd.xldate_as_datetime(sheet.cell_value(row, 8), workbook.datemode).date(),
                # Assuming date of birth is in column 9 (index 8)
                'nationality': sheet.cell_value(row, 9),  # Assuming nationality is in column 10 (index 9)
                'identification_no': sheet.cell_value(row, 10),
                # Assuming identification number is in column 11 (index 10)
                'passport_no': sheet.cell_value(row, 11),  # Assuming passport number is in column 12 (index 11)
                'visa_no': sheet.cell_value(row, 12),  # Assuming visa number is in column 13 (index 12)
                'work_permit_no': sheet.cell_value(row, 13),  # Assuming work permit number is in column 14 (index 13)
                'visa_expire_date': xlrd.xldate_as_datetime(sheet.cell_value(row, 14), workbook.datemode).date() if sheet.cell_type(row, 14) == xlrd.XL_CELL_DATE else None,
                'image': None,  # Placeholder for employee image (you need to handle image data appropriately)
            }

            # Create employee record
            Employee.create(employee_vals)
