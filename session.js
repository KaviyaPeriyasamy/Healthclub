// Copyright (c) 2021, Bluelynx and contributors
// For license information, please see license.txt

frappe.ui.form.on('Session', {
	refresh(frm) {
		if (frm.doc.docstatus === 1){
		frm.add_custom_button(__("Create"), function() {
			frm.trigger("make_payment");
		  },__("Payment"));
		frm.add_custom_button(__("View"),
			function(){ frappe.set_route('List', 'Payment',
			{'session_doc': frm.doc.name});},__("Payment"));
	}
	if(frm.doc.payment_status =="Paid"){
		frm.remove_custom_button('Create','Payment');
	}
	},
	make_payment: function(frm){
		frappe.model.open_mapped_doc({
			method: "healthclub.healthclub.doctype.session.session.make_payment",
			frm: cur_frm,
			freeze_message: __("Creating Payment ...")
		})
	},
	is_group:function(frm){
		if(!frm.doc.is_group){
			frm.set_value("quantity","")
		}
		if(!frm.doc.quantity){calculate_item_values(frm);}
	},
	quantity:function(frm){
		calculate_item_values(frm);
	},
	user_type:function(frm){
		if(frm.doc.user_type=="Member" || frm.doc.user_type=="Guest"){
		 frm.set_value("user_id","")
		 frm.set_value("user_name","")
		 frm.set_value("mobile_number","")
		}
	},
});
frappe.ui.form.on('Session Item', {
	choose_sessions_remove:function(frm){
		calculate_item_values(frm);
	},
	amount_qar:function(frm,cdt,cdn){
		calculate_item_values(frm);
	}
});
var calculate_item_values= function(frm) {
	let final_total = 0;
	frm.doc.choose_sessions.forEach(function(t){
	if(frm.doc.quantity){
		t.amount_qar = t.amount_qar * frm.doc.quantity
	}
	final_total += t.amount_qar
	})
	frm.set_value("total_amount_qar", Math.ceil(final_total));
}