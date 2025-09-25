from odoo import models, fields,api,_
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """Block SO confirmation unless the customer is Approved."""
        for order in self:
            if order.partner_id.state != 'approved':
                raise UserError("The Selected Partner Must be Approved to Confirm the Sale Order!")
        return super(SaleOrder, self).action_confirm()