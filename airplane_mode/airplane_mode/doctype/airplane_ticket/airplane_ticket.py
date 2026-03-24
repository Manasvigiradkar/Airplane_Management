import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Ticket cannot be submitted unless status is 'Boarded'.")

    # 1️⃣ Auto assign seat before insert
    def before_insert(self):
        self.assign_seat()

    def assign_seat(self):
        number = random.randint(1, 99)
        letter = random.choice(["A", "B", "C", "D", "E"])
        self.seat = f"{number}{letter}"

    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total_amount()

    # -----------------------------
    # Remove duplicate add-ons
    # -----------------------------
    def remove_duplicate_add_ons(self):
        seen = set()
        unique_add_ons = []

        for row in self.add_ons:
            if row.item not in seen:
                seen.add(row.item)
                unique_add_ons.append(row)

        self.set("add_ons", unique_add_ons)

    # -----------------------------
    # Calculate total amount
    # -----------------------------
    def calculate_total_amount(self):
        add_on_total = sum(row.amount or 0 for row in self.add_ons)
        self.total_amount = (self.flight_price or 0) + add_on_total
