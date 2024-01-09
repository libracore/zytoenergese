frappe.ui.form.on('Sales Order Item', {
	is_inclusive(frm, cdt, cdn) {
	    var row = locals[cdt][cdn];
		if (row.is_inclusive === 1) {
		    frappe.model.set_value(cdt, cdn, "rate", 0);
		} else {
		    frappe.model.set_value(cdt, cdn, "rate", row.price_list_rate);
		}
	}
});
