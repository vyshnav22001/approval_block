from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    amount_computation = fields.Integer(compute='_compute_full_amount',
                                        store=True, string='Approval Block')

    @api.depends('amount_total')
    def _compute_full_amount(self):
        amnt_limit = self.env['approval.block.record'].search([])
        limit = amnt_limit.mapped('amount_limit')
        limit.sort()

        for amount in limit:
            if amount > self.amount_total:
                self.amount_computation = amount
                break
            else:
                self.amount_computation = ""

