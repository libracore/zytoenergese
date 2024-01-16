# Copyright (c) 2013, libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data
	
def get_columns():
	columns = [
		{"label": _("Device type"), "fieldname": "device_type", "fieldtype": "Data", "width": 90},
		{"label": _("Device Name"), "fieldname": "device_name", "fieldtype": "Data", "width": 90},
		{"label": _("Sales Order"), "fieldname": "to_order", "fieldtype": "Data", "width": 90},
		{"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 120},
		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 70},
		{"label": _("Maintenance Contract"), "fieldname": "maintenance_contract", "fieldtype": "Check", "width": 40},
		{"label": _("Old Maintenance Contract"), "fieldname": "old_maintenance_contract", "fieldtype": "Check", "width": 40},
		{"label": _("Rent Start"), "fieldname": "rent_start", "fieldtype": "Date", "width": 90},
		{"label": _("Rent End"), "fieldname": "rent_end", "fieldtype": "Date", "width": 90},
		{"label": _("Contract Start"), "fieldname": "contract_start", "fieldtype": "Date", "width": 90},
		{"label": _("First Invoice Due"), "fieldname": "first_invoice", "fieldtype": "Date", "width": 90},
		{"label": _("Invoice Created"), "fieldname": "invoice_created", "fieldtype": "Check", "width": 40}
	]
	return columns

def get_data(filters):
	
	sql_query = """SELECT
		`device_type`,
		`device_name`,
		`to_order`,
		`customer_name`,
		`transaction_type`,
		`with_maintenance_contract_check` AS `maintenance_contract`,
		`with_old_maintenance_contract` AS `old_maintenance_contract`,
		`rent_start`,
		`rent_end`,
		`maintenance_contract_start` AS `contract_start`,
		`first_invoice_due` AS `first_invoice`,
		`invoice_created`
		FROM `tabDevice`"""
	
	if filters.invoice_maintenance_contract:
		sql_query += """
			WHERE `first_invoice_due` > '{today}'
			AND `invoice_created` = 0
		"""
		
	data = frappe.db.sql(sql_query, as_dict=True)
	
	return data
