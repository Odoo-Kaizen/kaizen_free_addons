# Copyright 2025 Kaizen Principles

from odoo import api, fields, models


class SaleOrder(models.Model):
    """
    Inherit Sales Orders to include a Payment Method (Cash/Bank journal)
    that auto-fills from the related customer's default preference.
    """
    _inherit = "sale.order"

    payment_method_id = fields.Many2one(
        "account.journal",
        domain=[("type", "in", ["bank", "cash"])],
        string="Payment Method",
        help="Journal (Cash/Bank) to be used for this Sales Order.",
    )

    @api.onchange("partner_id")
    def _onchange_partner_id_warning(self):
        """
        On customer change, prefill the Sales Order payment method with the
        customer's default Sale Payment Method, if any.
        """
        res = super()._onchange_partner_id_warning()
        if self.partner_id.commercial_partner_id.sale_payment_method_id:
            self.payment_method_id = (
                self.partner_id.commercial_partner_id.sale_payment_method_id.id
            )
        elif self.partner_id.sale_payment_method_id:
            # Assign the record (not just ID) to avoid edge cases
            self.payment_method_id = self.partner_id.sale_payment_method_id.id
        return res
