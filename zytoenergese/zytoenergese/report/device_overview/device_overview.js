// Copyright (c) 2016, libracore AG and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Device Overview"] = {
	"filters": [
		{
			"fieldname":"invoice_maintenance_contract",
			"label": __("Invoice Maintenance Contract"),
			"fieldtype": "Check"
		}
	]
};
