// Copyright (c) 2016, Bluelynx and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Payment Type Report"] = {
	"filters": [
		{
			"fieldname": "date",
			"label": __("Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd":1
		},
		{
			"fieldname": "payment_mode",
			"label": __("Payment Mode"),
			"fieldtype": "Link",
			"options": "Payment Mode"
		}
	]
};