{
    "name": "Kaizen Base Utilities (Arabic Amount-in-Words, Record Insights & Dev Tools)",
    "summary": "Arabic amount-in-words, Arabic numerals for QWeb, record inspector, sequence guard, server action helpers, cache mixin, and a /ping healthcheck.",
    "description": """
        Key features
        ------------
        • Arabic amount-in-words for invoices/receipts (SAR, AED, JOD, BHD, SYP + generic).
        • QWeb helpers: Arabic digits (٠١٢٣...) and amount-to-text available in reports.
        • Record Inspector dialog: creation/modification details, audit log & chatter diffs.
        • Server Action context extras: json, regex, logger().
        • Cache mixin for performant reads.
        • Sequence guard with clear error if sequence missing.
        • Developer utilities (external ID suggestion/creation, one2many view action, hierarchical sort, random password).
        • Backend improvements for menu debug, ACL editing (ACE widget), and module search filter.
        Intended for Arabic-speaking implementations and developer toolkits.
        """,
    "version": "17.0.1.0",
    "category": "Technical",
    "author": "Kaizen Principles",
    "website": "http://www.kaizenae.com/",
    "license": "LGPL-3",
	'images':[
        'static/description/banner.gif'
	],
    "depends": [
        'base', 'web'
    ],
    "data": [
        'view/ir_module_module.xml',
        'view/ir_rule.xml',
        'view/ir_ui_menu.xml',
        'view/ir_actions_server.xml',
        'view/ir_ui_view.xml',
        'view/ir_model_fields.xml',
        "view/ir_default.xml",
        'view/action.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'kaz_base/static/src/js/*.js',
            'kaz_base/static/src/xml/*.xml'
        ]
    },        
    'post_init_hook' : 'post_init_hook',
    'installable': True,
}

