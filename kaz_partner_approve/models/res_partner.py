##
from odoo import models, fields, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    approval_note = fields.Char(string="Approval Note", help="Optional reason for approving or resetting to draft.",tracking=True)
    state = fields.Selection([('draft','Draft'),('approved', 'Approved')], string="Approve Status", default="draft", tracking=True)

    def action_verify(self):
        """Approve partner(s)."""
        if not self.env.user.has_group('kaz_partner_approve.group_verify_partner'):
            raise UserError(_("You do not have permission to approve partners."))
        for rec in self:
            rec.state = 'approved'
            if rec.approval_note:
                rec.message_post(body=_("Approved: %s") % rec.approval_note)
                rec.approval_note = False

    def action_draft(self):
        """Reset partner(s) to Draft. Context flag 'reset' is used to allow write()."""
        if not self.env.user.has_group('kaz_partner_approve.group_verify_partner'):
            raise UserError(_("You do not have permission to reset partners to draft."))
        for rec in self:
            rec.with_context(reset=True).write({'state': 'draft'})
            if rec.approval_note:
                rec.message_post(body=_("Reset to Draft: %s") % rec.approval_note)
                rec.approval_note = False

    def write(self, vals):
        """
        Prevent modifying sensitive partner data once Approved.
        To change an Approved partner, first set it back to Draft via action_draft().
        """
        for rec in self:
            monitored_fields = {'name', 'sub_company_type', 'parent_id', 'type',
                                'street', 'company_name',
                                'street2', 'city', 'state_id', 'zip', 'country_id',
                                'vat', 'nationality', 'passport', 'ssn_id', 'visa',
                                'function', 'phone', 'mobile', 'email', 'website',
                                'title', 'category_id', 'child_ids', 'is_contractor',
                                'is_tenant', 'is_owner', 'is_agency', 'is_supplier',
                                'is_resident', 'user_id', 'team_id', 'property_payment_term_id',
                                'buyer_id', 'property_supplier_payment_term_id', 'bank_ids',
                                'receipt_reminder_email', 'property_purchase_currency_id',
                                'property_account_position_id', 'company_registry',
                                'ref', 'company_id', 'property_stock_customer',
                                'property_stock_supplier', 'property_account_receivable_id',
                                'property_account_payable_id'
                                }
            if not rec._context.get('reset') and not self._context.get('active_model'):
                if rec.state == 'approved' and vals.get('state') != 'draft':
                    if monitored_fields & vals.keys():
                        raise UserError(_("You cannot modify an approved partner record."))
        return super().write(vals)
        
