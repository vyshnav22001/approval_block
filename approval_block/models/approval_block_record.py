from odoo import api, fields, models


class ApprovalBlockRecord(models.Model):
    _name = "approval.block.record"
    _description = "Approval block records"
    _rec_name = 'amount_limit'

    name = fields.Char(string='Name of the Block', compute='_compute_name')
    company_id = fields.Many2one('res.company', copy=False,
                                 string="Company",
                                 default=lambda
                                     self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda
                                  self: self.env.user.company_id.currency_id.id)
    amount_limit = fields.Monetary(string='Amount Limit')
    block_message = fields.Text(string='Block Message')

    @api.depends('amount_limit')
    def _compute_name(self):
        for rec in self:
            rec.name = 'Block of' + ' ' + str(rec.amount_limit)
