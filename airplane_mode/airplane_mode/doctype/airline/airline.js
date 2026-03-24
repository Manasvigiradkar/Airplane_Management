frappe.ui.form.on("Airline", {
    refresh(frm) {

        if (frm.doc.website) {

            frm.add_custom_button("Open Website", function() {
                window.open(frm.doc.website);
            }, "Links");

        }

    }
});