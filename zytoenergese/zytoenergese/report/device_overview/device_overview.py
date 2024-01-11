# Copyright (c) 2013, libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data
	
def get_columns():
	columns = [
		{"label": _("Device type"), "fieldname": "device_type", "fieldtype": "Data", "width": 100},
		{"label": _("Device Name"), "fieldname": "device_name", "fieldtype": "Data", "width": 100},
		{"label": _("Sales Order"), "fieldname": "to_order", "fieldtype": "Data", "width": 100},
		{"label": _("Customer"), "fieldname": "customer", "fieldtype": "Data", "width": 100},
		{"label": _("Transaction Type"), "fieldname": "transaction_type", "fieldtype": "Data", "width": 100},
