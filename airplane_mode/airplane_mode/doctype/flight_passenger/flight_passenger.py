import frappe
from frappe.model.document import Document

class FlightPassenger(Document):

    def before_save(self):
        self.set_full_name()

    def set_full_name(self):
        first = self.first_name or ""
        last = self.last_name or ""
        self.full_name = f"{first} {last}".strip()
