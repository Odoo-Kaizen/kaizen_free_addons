# Copyright 2025 Kaizen Principles

from odoo import models


class PartnerXlsx(models.AbstractModel):
    """
    Sample concrete report to demonstrate usage: prints partner names in column A.
    """
    _name = "report.kaz_report_xlsx.partner_xlsx"
    _inherit = "report.kaz_report_xlsx.abstract"
    _description = "Partner XLSX Report"

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet("Report")
        for i, obj in enumerate(partners):
            bold = workbook.add_format({"bold": True})
            sheet.write(i, 0, obj.name, bold)
