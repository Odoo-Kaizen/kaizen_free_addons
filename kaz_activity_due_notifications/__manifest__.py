# -*- coding: utf-8 -*-
{
    "name": "Kaizen - Activity Due Notifications",
    "summary": "Configurable reminders for Odoo Activities: notify before, on, or after due date with flexible offsets.",
    "description": """
Kaizen - Activity Due Notifications
===================================

Ensure your team never misses a follow-up. This module adds company-level
settings to enable Activity reminders in Odoo and configure when to notify:
before the due date, on the due date, and/or after the due date—using
customizable day offsets. You can optionally notify the activity creator
to drive ownership and accountability.

Key Features
------------
- Company-level toggle for activity due notifications
- Notify before / on / after due date with day offsets
- Option to notify the activity creator
- Works across apps that use Odoo Activities (CRM, Accounting, Projects, etc.)
- Clean settings UI under General Settings
- Multi-company ready
""",
    "version": "17.0.1.0",
    "author": "Kaizen Principles",
    "website": "http://www.kaizenae.com/",
    "depends": [
        'mail'
    ],
    "data": [
        'views/res_config_settings_views.xml',
    ],
    "images": ["static/description/banner.gif", ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
}
