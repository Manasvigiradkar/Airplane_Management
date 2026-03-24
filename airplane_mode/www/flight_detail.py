import frappe

def get_context(context):
    name = frappe.form_dict.get("name")

    if not name:
        frappe.throw("Flight not found")

    flight = frappe.get_doc("Airplane Flight", name)

    # Convert duration (seconds → hours & minutes)
    total_seconds = flight.duration or 0
    total_seconds = float(total_seconds)

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    context.flight = flight
    context.duration_formatted = f"{hours}h {minutes}m"
