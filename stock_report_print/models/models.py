# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def print_valuation_report(self):
        return self.env.ref('stock_report_print.action_print_inventory_stock_report').report_action(self, data=None)

    def _get_report_base_filename(self):
        return 'Inventory Stock Report' + str(fields.Datetime.now().strftime('%Y-%m-%d %H:%M'))

    @api.model
    def get_report_date(self):
        return str(fields.Datetime.now().strftime('%Y-%m-%d %H:%M'))

    total_purchased = fields.Float(
        string='Total Purchase',
        required=False, compute='_compute_totals_purchases')
    total_sales_product = fields.Float(
        string='Total Sold',
        required=False, compute='_compute_totals_sales')

    avg_cost = fields.Float(string='Average Cost', compute='_compute_avg_cost')
    total_value = fields.Float(string='Total Value', compute='_compute_total_value')

    def _compute_avg_cost(self):
        for product in self:
            product.avg_cost = product.standard_price

    @api.depends('qty_available', 'standard_price')
    def _compute_total_value(self):
        for product in self:
            product.total_value = product.qty_available * product.standard_price

    def _compute_totals_purchases(self):
        domain = [
            ('order_id.state', 'in', ['purchase', 'done']),
            ('product_id', 'in', self.ids),
        ]
        # Odoo 19 _read_group returns a list of tuples (product_id, sum_qty)
        # groupby=['product_id'], aggregates=['product_uom_qty:sum']
        groups = self.env['purchase.order.line']._read_group(
            domain, 
            groupby=['product_id'], 
            aggregates=['product_uom_qty:sum']
        )
        # groups is [(product_record, sum_qty), ...]
        purchased_data = {group[0].id: group[1] for group in groups}
        
        for product in self:
            product.total_purchased = float_round(purchased_data.get(product.id, 0),
                                                  precision_rounding=product.uom_id.rounding)

    def _compute_totals_sales(self):
        r = {}
        # self.sales_count = 0 # sales_count is typically a computed field, setting it here might not be useful or could error if it's read-only

        done_states = self.env['sale.report']._get_done_states()

        domain = [
            ('state', 'in', done_states),
            ('product_id', 'in', self.ids),
        ]
        
        # Odoo 19 _read_group
        groups = self.env['sale.report']._read_group(
            domain, 
            groupby=['product_id'], 
            aggregates=['product_uom_qty:sum']
        )
        r = {group[0].id: group[1] for group in groups}

        for product in self:
            product.total_sales_product = float_round(r.get(product.id, 0), precision_rounding=product.uom_id.rounding)
        return r
