# -*- coding: utf-8 -*-
# Copyright (c) 2021, Bluelynx and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class Session(Document):
	pass

@frappe.whitelist()
def make_payment(source_name, target_doc=None):
	doc = get_mapped_doc("Session", source_name,	{
		"Session": {
			"doctype": "Payment",
			"field_map": {
				"name": "session_doc",
				"user_id": "user_id",
				"type": "payment_type",
				"total_amount_qar": "session_amount",
				"choose_sessions": "sessions_table",
			}
			}
		}, target_doc)
	return doc
