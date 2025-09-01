# Copyright 2025 Kaizen Principles

from odoo import fields, models


class ResPartner(models.Model):
    """
    Extends Contacts to store a default Sale Payment Method (Cash/Bank journal)
    used to auto-fill Sales Orders for this customer.
    """
    _inherit = "res.partner"

    sale_payment_method_id = fields.Many2one(
        "account.journal",
        domain=[("type", "in", ["bank", "cash"])],
        string="Sale Payment Method",
        help="Default journal (Cash/Bank) used to prefill Sales Orders for this customer.",
        copy=False,
    )
