import frappe

def get_context(context):
    flights = frappe.get_all(
        "Airplane Flight",
        filters={"is_published": 1},
        fields=[
            "name",
            "airplane",
            "source_airport_code",
            "destination_airport_code",
            "date_of_departure",
            "time_of_departure",
            "duration"
        ]
    )

    # Convert duration for each flight
    for flight in flights:
        total_seconds = float(flight.duration or 0)

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)

        flight.duration_formatted = f"{hours}h {minutes}m"

    context.flights = flights
