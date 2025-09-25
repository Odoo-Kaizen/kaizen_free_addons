{
    "name": "Kaizen - Partner Approval Gate",
    "summary": "Block SO/PO confirmation, invoice & payment posting, and picking validation until partner is Approved. Adds Draft/Approved workflow with a Partner Manager role.",
    "description": """
Partner Approval Gate by Kaizen Principles

• Enforce partner vetting with a Draft → Approved workflow.
• Prevent Sales Order / Purchase Order confirmation if partner is not Approved.
• Prevent posting Customer Invoices / Vendor Bills and Payments until Approved.
• Prevent Stock Picking validation until Approved.
• Bulk Approve / Set to Draft from list view.
• Dedicated 'Partner Manager' group controls approvals.

Ideal for companies that require KYC/compliance before transacting with customers/vendors.
""",
    "version": "17.0.1.0",
    "category": "Contacts",
    "author": "Kaizen Principles",
    "website": "http://www.kaizenae.com/",
    "license": "LGPL-3",
    'description': """
            This module helps to manage the Customer / Supplier approval process with Draft & Approve Stages. Sales Order / Purchase Order can be confirmed & Invoice can be Posted only when the Partner is in Approved Stage..
    """,
    'images': ['static/description/banner.gif',],
    'depends': ['sale','purchase','account','stock','contacts'],
    'data': [
        'security/security.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
