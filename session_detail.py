from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	if filters:
		columns = get_column()
		data = get_data(filters)
	return columns, data

def get_column():
	columns = [
		{
		"label": "Session",
		"fieldname": "session",
		"fieldtype": "Link",
        "options": "Session",
		"width": 100
	    },
        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": "User Type",
            "fieldname": "user_type",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "User ID",
            "fieldname": "user_id",
            "fieldtype": "Dynamic Link",
            "options": "user_type",
            "width": 100
        },
        {
            "label": "User Name",
            "fieldname": "user_name",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Mobile Number",
            "fieldname": "mobile_number",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Is Group",
            "fieldname": "is_group",
            "fieldtype": "Check",
            "width": 100
        },
        {
            "label": "Qty",
            "fieldname": "qty",
            "fieldtype": "Int",
            "width": 100
        },
        {
            "label": "Session Plan",
            "fieldname": "session_plan",
            "fieldtype": "Link",
            "options": "Session Plan",
            "width": 100
        },
        {
            "label": "Sessions",
            "fieldname": "sessions",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Amount (QAR)",
            "fieldname": "amount_qar",
            "fieldtype": "Currency",
            "width": 100
        },
        {
            "label": "Total Amount",
            "fieldname": "total_amount",
            "fieldtype": "Currency",
            "width": 100
        },
        {
            "label": "Payment Status",
            "fieldname": "payment_status",
            "fieldtype": "Data",
            "width": 200
        }
	]
	return columns

def get_data(filters):
	data =[]
	data = frappe.db.sql('''
				select se.name as session, se.date as date, se.user_type as user_type,
				se.user_id as user_id, se.user_name as user_name, se.mobile_number as mobile_number,
				se.is_group as is_group, se.quantity as quantity, se.total_amount_qar as total_amount, 
				se.payment_status as payment_status,
				sei.session_plan as session_plan, sei.sessions as sessions, sei.amount_qar as amount_qar
				from `tabSession` se inner join `tabSession Item` sei
				on sei.parent = se.name
				where se.date between %s and %s''',
				(filters['from_date'],filters['to_date']),  as_dict = True)
	return data
