import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data()

    total = sum(d["revenue"] for d in data)

    data.append({
        "airline": "Total",
        "revenue": total
    })

    chart = get_chart(data[:-1])
    summary = get_summary(data[:-1])

    return columns, data, None, chart, summary


def get_columns():
    return [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_data():
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []

    for airline in airlines:
        airplanes = frappe.get_all(
            "Airplane",
            filters={"airline": airline.name},
            fields=["name"]
        )

        airplane_names = [a.name for a in airplanes]

        if not airplane_names:
            data.append({"airline": airline.name, "revenue": 0})
            continue

        flights = frappe.get_all(
            "Airplane Flight",
            filters={"airplane": ["in", airplane_names]},
            fields=["name"]
        )

        flight_names = [f.name for f in flights]

        if not flight_names:
            data.append({"airline": airline.name, "revenue": 0})
            continue

        tickets = frappe.get_all(
            "Airplane Ticket",
            filters={
                "flight": ["in", flight_names],
                "docstatus": 1
            },
            fields=["flight_price"]
        )

        revenue = sum(t.flight_price for t in tickets if t.flight_price)

        data.append({
            "airline": airline.name,
            "revenue": revenue
        })

    return data


def get_chart(data):
    return {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [{"values": [d["revenue"] for d in data]}]
        },
        "type": "donut"
    }


def get_summary(data):
    total = sum(d["revenue"] for d in data)

    return [{
        "value": total,
        "indicator": "Green",
        "label": "Total Revenue",
        "datatype": "Currency"
    }]