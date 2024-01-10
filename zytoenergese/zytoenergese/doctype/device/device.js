// Copyright (c) 2023, libracore AG and contributors
// For license information, please see license.txt

frappe.ui.form.on('Device', {
	validate: function(frm) {
		check_for_so(frm);
	}
});

function check_for_so(frm) {
	if ((frm.doc.with_old_maintenance_contract == 0) && (!frm.doc.to_order)) {
		frappe.msgprint( __("Please set a Sales Order"), __("Validation") );
		frappe.validated=false;
	}
}
