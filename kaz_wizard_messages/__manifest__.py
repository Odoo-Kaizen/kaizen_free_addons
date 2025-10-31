{
	"name": "Kaizen Message Wizard",
    "summary": "Show rich, translatable pop‑up messages, warnings, and summaries anywhere in Odoo.",
    "description": """
    Kaizen Message Wizard
    A lightweight, reusable wizard to display formatted messages (warnings, success notices, operation summaries) in a modal dialog.
    - One-line API from any model/server action
    - HTML rendering for clearer communication
    - Consistent UX and fully translatable
    - Transient by design; no long-term storage
    Use cases: confirmations after imports or postings, blocking warnings before irreversible actions, and short "next steps" guidance.
    """,
	"sequence": 1,
	"version": "18.0.1.0.1",
    "author": "Kaizen Principles",
    "website": "http://www.kaizenae.com/",
	"license":  "LGPL-3",
	"data": [
		'security/ir.model.access.csv',
		'wizard/wizard_message.xml'],
	"images": ['static/description/Banner.png'],
	"pre_init_hook": "pre_init_check",
}