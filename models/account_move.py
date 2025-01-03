from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _get_invoices_domain(self):
        if self.env.user.has_group('base.group_portal'):
            sale_orders = self.env['sale.order'].search([('create_uid', '=', self.env.user.id)])
            return [('id', 'in', sale_orders.mapped('invoice_ids').ids)]
        return super(AccountMove, self)._get_invoices_domain()

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(AccountMove, self).fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type == 'tree' and self.env.user.has_group('base.group_portal'):
            domain = self._get_invoices_domain()
            res['fields']['partner_id']['domain'] = domain
        return res