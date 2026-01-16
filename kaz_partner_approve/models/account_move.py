from odoo import models, fields,api,_
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        """
            Prevent posting invoices/bills if the partner is not Approved.
            Vendor bills ('in_invoice') have their own explicit message;
            all other move types reuse the generic message.
        """
        for invoice in self:
            if invoice.partner_id:
                if invoice.partner_id.state != 'approved' and invoice.move_type == 'in_invoice':
                    raise UserError("The selected Partner Must be Approved to Post the Vendor Bill!")
                elif invoice.partner_id.state != 'approved':
                    raise UserError("The selected Partner Must be Approved to Post the Invoice!")
        return super().action_post()
