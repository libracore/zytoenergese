// Copyright (c) 2021-2024, libracore AG and contributors
// For license information, please see license.txt


$(document).ready(function() {
	setTimeout(function(){
		var company = frappe.defaults.get_user_default("Company")
		console.log(company);
		var navbars = document.getElementsByClassName("navbar");
		if (navbars.length > 0) {
			if (company == "iNCO Beauty-Line GmbH") {
				navbars[0].style.backgroundColor = "#B0473A";
			} else if (company == "iNCO Natural GmbH") {
				navbars[0].style.backgroundColor = "#229954";
			} else {
				navbars[0].style.backgroundColor = "#33ecff";
			}
		}
	}, 1000);
});
