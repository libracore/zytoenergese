from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Selling"),
            "icon": "fa fa-tools",
            "items": [
				{
                   "type": "doctype",
                   "name": "Customer",
                   "label": _("Customer"),
                   "description": _("Customer")
                },
                {
                   "type": "doctype",
                   "name": "Quotation",
                   "label": _("Quotation"),
                   "description": _("Quotation")
                },
                {
                   "type": "doctype",
                   "name": "Sales Order",
                   "label": _("Sales Order"),
                   "description": _("Sales Order")
                },
                {
                   "type": "doctype",
                   "name": "Delivery Note",
                   "label": _("Delivery Note"),
                   "description": _("Delivery Note")
                },
                {
                   "type": "doctype",
                   "name": "Sales Invoice",
                   "label": _("Sales Invoice"),
                   "description": _("Sales Invoice")
                }
            ]
        },
        {
            "label": _("Buying"),
            "icon": "fa fa-tools",
            "items": [
                {
                   "type": "doctype",
                   "name": "Supplier",
                   "label": _("Supplier"),
                   "description": _("Supplier")
                },
                {
                   "type": "doctype",
                   "name": "Purchase Invoice",
                   "label": _("Purchase Invoice"),
                   "description": _("Purchase Invoice")
                }
            ]
        },
        {
            "label": _("Item"),
            "icon": "fa fa-tools",
            "items": [
                {
                   "type": "doctype",
                   "name": "Item",
                   "label": _("Item"),
                   "description": _("Item")
                },
                {
                   "type": "doctype",
                   "name": "Price List",
                   "label": _("Price List"),
                   "description": _("Price List")
                },
                {
                   "type": "doctype",
                   "name": "Device",
                   "label": _("Device"),
                   "description": _("Device")
                },
                {
                   "type": "report",
                   "name": "Device Overview",
                   "label": _("Device Overview"),
                   "description": _("Device Overview")
                }
            ]
        },
        {
            "label": _("Accounting"),
            "icon": "fa fa-tools",
            "items": [
                {
                   "type": "doctype",
                   "name": "Supplier",
                   "label": _("Supplier"),
                   "description": _("Supplier")
                },
                {
                   "type": "doctype",
                   "name": "Purchase Invoice",
                   "label": _("Purchase Invoice"),
                   "description": _("Purchase Invoice")
                },
                {
                   "type": "doctype",
                   "name": "Payment Proposal",
                   "label": _("Payment Proposal"),
                   "description": _("Payment Proposal")
                },
                {
                   "type": "page",
                   "name": "bank_wizard",
                   "label": _("Bank wizard"),
                   "description": _("Bank wizard")
                },
                {
                   "type": "doctype",
                   "name": "Journal Entry",
                   "label": _("Journal Entry"),
                   "description": _("Journal Entry")
                }
            ]
        }
    ]
