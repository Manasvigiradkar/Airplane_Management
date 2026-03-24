import frappe
import random


def execute():
    # Get all tickets where seat is empty or null
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"seat": ["in", ["", None]]},
        fields=["name"]
    )

    for ticket in tickets:
        doc = frappe.get_doc("Airplane Ticket", ticket.name)

        # Generate random seat
        number = random.randint(1, 99)
        letter = random.choice(["A", "B", "C", "D", "E"])
        seat = f"{number}{letter}"

        # Update seat without triggering validations
        doc.db_set("seat", seat)

    frappe.db.commit()
