frappe.ui.form.on('Customer', {
    before_save(frm) {
        if (!frm.doc.__islocal) {
            set_primary_address(frm);
        }
    }
});

function set_primary_address(frm) {
    frappe.call({
        'method': 'erpnextswiss.scripts.crm_tools.get_primary_customer_contact',
        'args': {
            'customer': frm.doc.name
        },
        'async': false,
        'callback': function(response) {
            if (response.message) {
                var contact = response.message;
                var full_name = contact.first_name + " " + contact.last_name;
                cur_frm.set_value('primary_contact', full_name);
            }
        }
    });
}
