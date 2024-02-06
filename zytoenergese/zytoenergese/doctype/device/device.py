# -*- coding: utf-8 -*-
# Copyright (c) 2023, libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Device(Document):
	pass

def get_devices_for_auto_repeat(sales_invoice, device_type):		
	sql_query = """
		SELECT DISTINCT `device`.`device_name`
		FROM `tabSales Invoice` AS `invoice`
		LEFT JOIN `tabAuto Repeat` AS `repeat` ON `invoice`.`auto_repeat` = `repeat`.`name`
		LEFT JOIN `tabSales Invoice Item` AS `item` ON `item`.`parent` = `repeat`.`reference_document`
		LEFT JOIN `tabDevice` AS `device` ON `item`.`sales_order` = `device`.`to_order`
		WHERE `invoice`.`name` = '{invoice_name}'
		AND `device`.`device_type` = '{device_type}'
		AND `device`.`device_returned` = 0
		""".format(invoice_name=sales_invoice, device_type=device_type)
		
	devices = frappe.db.sql(sql_query, as_dict=True)
	
	return devices
