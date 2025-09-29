from odoo import models, fields,api,_
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        """Block stock picking validation unless the partner is Approved."""
        for invoice in self:
            if invoice.partner_id.state != 'approved':
                raise UserError("The Selected Partner Must be Approved to Validate the Picking!")
        return super(StockPicking, self).button_validate()