import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
class AirplaneFlight(Document):
    
    website = True

    def on_submit(self):
        self.status = "Completed"
