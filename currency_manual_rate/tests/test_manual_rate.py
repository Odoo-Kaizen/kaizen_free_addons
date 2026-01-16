# -*- coding: utf-8 -*-
from odoo.tests import tagged
from odoo.tests.common import TransactionCase
from odoo import fields

@tagged('post_install', '-at_install')
class TestManualCurrencyRate(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.currency_usd = cls.env.ref('base.USD')
        cls.currency_eur = cls.env.ref('base.EUR')
        # Ensure EUR is not base currency, assuming company currency is USD or we setup rates relative to company
        cls.company_currency = cls.env.company.currency_id
        
        # Setup currency rates
        if cls.company_currency != cls.currency_usd:
             cls.currency_usd.rate_ids.create({
                'rate': 1.0,
                'name': fields.Date.today(),
                'company_id': cls.env.company.id,
             })
        
        cls.partner = cls.env['res.partner'].create({'name': 'Test Partner'})
        cls.product = cls.env['product.product'].create({'name': 'Test Product', 'list_price': 100.0})

    def test_manual_currency_rate(self):
        """ Test that manual currency rate is applied correctly """
        
        # Create invoice with manual rate
        invoice = cls.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner.id,
            'currency_id': self.currency_eur.id if self.company_currency != self.currency_eur else self.currency_usd.id,
            'invoice_date': fields.Date.today(),
            'apply_currency_rate': True,
            'manual_rate': 2.5,
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': self.product.id,
                    'price_unit': 100.0,
                }),
            ],
        })

        # Check if rate is applied to lines
        for line in invoice.invoice_line_ids:
            self.assertEqual(line.currency_rate, 2.5, "Manual currency rate was not applied to invoice line")

        # Change manual rate
        invoice.write({'manual_rate': 3.0})
        # Trigger recompute or check if it updates automatically (might need to trigger recompute manually in test or via write)
        # In Odoo UI, write triggers recompute.
        
        for line in invoice.invoice_line_ids:
             self.assertEqual(line.currency_rate, 3.0, "Updated manual currency rate was not applied")

    def test_manual_rate_disabled(self):
        """ Test that manual rate is ignored when checkbox is unchecked """
        invoice = cls.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner.id,
            'currency_id': self.currency_eur.id if self.company_currency != self.currency_eur else self.currency_usd.id,
            'invoice_date': fields.Date.today(),
            'apply_currency_rate': False,
            'manual_rate': 5.0, # Should be ignored
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': self.product.id,
                    'price_unit': 100.0,
                }),
            ],
        })

        for line in invoice.invoice_line_ids:
            self.assertNotEqual(line.currency_rate, 5.0, "Manual rate applied even when disabled")

