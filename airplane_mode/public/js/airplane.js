frappe.ui.form.on('Airplane', {
    refresh: function(frm) {

        console.log("🔥 JS LOADED SUCCESSFULLY");

        frm.add_custom_button('Visit Website', function() {
            if (frm.doc.website) {
                window.open(frm.doc.website, '_blank');
            } else {
                frappe.msgprint("No website found");
            }
        }, 'View');

    }
});