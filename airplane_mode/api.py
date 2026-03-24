import frappe

@frappe.whitelist()
def get_fare_for_flight(flight):
    if not flight:
        return 0

    # Fetch flight document
    flight_doc = frappe.get_doc("Airplane Flight", flight)

    # Example pricing logic
    # ₹100 per minute
    rate_per_minute = 3

    duration = flight_doc.duration or 0
    fare = duration * rate_per_minute

    return fare
