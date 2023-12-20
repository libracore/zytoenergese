# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "zytoenergese"
app_title = "Zytoenergese"
app_publisher = "libracore AG"
app_description = "ERPNext Apps"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@libracore.com"
app_license = "AGPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zytoenergese/css/zytoenergese.css"
app_include_js = "/assets/zytoenergese/js/zytoenergese.js"

# include js, css files in header of web template
# web_include_css = "/assets/zytoenergese/css/zytoenergese.css"
# web_include_js = "/assets/zytoenergese/js/zytoenergese.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Customer" : "public/js/customer.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "zytoenergese.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "zytoenergese.install.before_install"
# after_install = "zytoenergese.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zytoenergese.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zytoenergese.tasks.all"
# 	],
# 	"daily": [
# 		"zytoenergese.tasks.daily"
# 	],
# 	"hourly": [
# 		"zytoenergese.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zytoenergese.tasks.weekly"
# 	]
# 	"monthly": [
# 		"zytoenergese.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "zytoenergese.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zytoenergese.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "zytoenergese.task.get_dashboard_data"
# }

