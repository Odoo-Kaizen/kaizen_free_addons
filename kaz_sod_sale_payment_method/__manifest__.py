# Copyright 2025 Kaizen Principles
{
    "name": "Kaizen – Default Payment Method on Customers & Sales Orders",
    "summary": "Auto-fill Sales Order payment method from the customer’s default Cash/Bank journal.",
    "description": """
        Kaizen – Default Payment Method on Customers & Sales Orders
        
        Overview :
            Set a default Cash/Bank journal on each customer and auto-fill that payment method on new Sales Orders.
            Reduce manual selection, prevent mistakes, and keep accounting data clean and consistent.
            
        Key Features :
        
            - Customer-level default payment method (Cash/Bank) 
            - Sales Order auto-fill from the customer's default
            - Clean, consistent accounting journals across teams
            - Seamless with Odoo Sales & Accounting (v18)

        Support:
            Built and maintained by Kaizen Principles (Odoo Gold Partner).
            For services and support, visit http://www.kaizenae.com/.
            """,
    "version": "17.0.1.0.0",
    "category": "Sale",
    "author": "Kaizen Principles",
    "website": "http://www.kaizenae.com/",
    "license": "LGPL-3",
    "depends": [
        "account",
        "sale",
    ],
    "data": [
        "views/res_partner_view.xml",
        "views/sale_view.xml",
    ],
    "images": ['static/description/banner.gif'],
}
