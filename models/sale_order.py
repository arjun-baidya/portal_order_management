from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # customer_id = fields.Many2one(
    #     'res.partner', string='Customer', required=True,
    #     help="Customer for whom the order is placed."
    # )

    # @api.model
    # def create(self, vals):
    #     if self.env.user.has_group('base.group_portal'):
    #         partner = self.env['res.partner'].browse(vals.get('customer_id'))
    #         if not partner:
    #             raise ValueError("Invalid customer.")
    #     return super(SaleOrder, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     if 'customer_id' in vals:
    #         # Logic to notify the selected customer via email can be added here
    #         pass
    #     return super(SaleOrder, self).create(vals)
