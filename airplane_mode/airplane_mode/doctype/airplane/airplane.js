frappe.ui.form.on('Airplane', {
    refresh: function(frm) {

        console.log("🔥 JS LOADED SUCCESSFULLY");

        if (frm.doc.website) {
            frm.add_custom_button('Visit Website', function() {
                window.open(frm.doc.website, '_blank');
            }, 'View');
        }

    }
});