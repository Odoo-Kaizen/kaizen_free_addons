from odoo import models, fields,api,_
from odoo.exceptions import UserError

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        """Block payment posting unless the related partner is Approved."""
        for invoice in self:
            if invoice.partner_id.state != 'approved':
                raise UserError("The Selected Partner Must be Approved to Confirm the Payment!")
        return super().action_post()