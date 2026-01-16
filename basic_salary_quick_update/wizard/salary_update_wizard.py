# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalaryUpdateWizard(models.TransientModel):
    _name = 'salary.update.wizard'

    type = fields.Selection(
        string='Type',
        selection=[('fixed', 'Fixed Amount'),
                   ('percent', 'Percent'), ],
        required=True,default='percent' )

    percent = fields.Float(
        string='Percent',
        required=False)
    amount = fields.Float(
        string='Amount',
        required=False)

    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Employees')

    def apply_update(self):
        for employee in self.employee_ids:
            # Assuming wage is available on hr.employee in Odoo 19 due to merge
            # or it writes to the current contract version.
            if self.type == 'fixed':
                employee.sudo().write({'wage': employee.wage + self.amount})
            elif self.type == 'percent':
                wage_addition = employee.wage * (self.percent / 100)
                employee.sudo().write({'wage': employee.wage + wage_addition})

