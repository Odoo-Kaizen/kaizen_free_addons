# Copyright (C) 2025 Kaizen Principles
{
    "name": "Kaizen - Excel (XLSX) Reports",
    "summary": "One-click Excel (.xlsx) report generation with optional attachments and smart filenames.",
    "description": """
    Generate professional Excel (.xlsx) reports directly from Odoo with one click.
    - Works from list/form views and supports wizard options.
    - Optional attachment saving per record for audit trails.
    - Smart filename evaluation via report settings.
    - Safe handling of duplicate sheet names.
        """,
    "author": "Kaizen Principles",
    "website": "http://www.kaizenae.com/",
    "category": "Reporting",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    'images': ['static/description/banner.gif',],
    "external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    "depends": ["base", "web"],
    "demo": ["demo/report.xml"],
    "installable": True,
    "assets": {
        "web.assets_backend": [
            "kaz_report_xlsx/static/src/js/report/action_manager_report.esm.js",
        ],
    },
}
