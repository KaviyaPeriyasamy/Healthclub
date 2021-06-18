# Copyright (c) 2013, Bluelynx and contributors
# For license information, please see license.txt

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
		"label": "Payment Mode",
		"fieldname": "payment_mode",
		"fieldtype": "Link",
		"options":"Payment Mode",
		"width": 100
	},
	{
		"label": "Amount",
		"fieldname": "amount",
		"fieldtype": "Currency",
		"width": 160
	}
	]
	return columns

def get_data(filters):
	data =[]
	payment_mode_list = []
	if 'payment_mode' in filters:
		payment_mode_list.append(filters['payment_mode'])
	else:
		payment_modes = frappe.get_list('Payment Mode')
		for mode in payment_modes:
			payment_mode_list.append(mode['name'])
	for mode in payment_mode_list:
		amount = sum([row['amount'] for row in frappe.db.get_list('Payment Item', {'payment_using': mode, 'payment_date':filters['date']}, ['amount'])])
		data.append({'payment_mode': mode, 'amount': amount})
	return data