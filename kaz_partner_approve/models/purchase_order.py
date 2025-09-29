from odoo import models, fields,api,_
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        """Block PO confirmation unless the vendor is Approved."""
        for order in self:
            if order.partner_id.state != 'approved':
                raise UserError("The Selected Partner Must be Approved to Confirm the Purchase Order!")
        return super(PurchaseOrder, self).button_confirm()