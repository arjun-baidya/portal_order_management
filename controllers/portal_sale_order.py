from odoo import http
from odoo.http import request

class PortalSaleOrder(http.Controller):

    @http.route('/my/order/create', type='http', website=True)
    def create_sale_order_form(self, **kwargs):
        customers = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
        products = request.env['product.product'].sudo().search([])
        return request.render('portal_order_management.create_sale_order_form_views', {
            'customers': customers,
            'products': products,
        })

    @http.route('/my/sale_order/submit', type='http', auth='user', website=True, csrf=True)
    def submit_sale_order(self, **post):
        customer_id = post.get('customer_id')
        print("customers   ", customer_id)
        product_ids = post.getlist('product_id[]') if hasattr(post, 'getlist') else post.get('product_id[]', '').split(
            ',')
        quantities = post.getlist('qty[]') if hasattr(post, 'getlist') else post.get('qty[]', '').split(',')
        price_units = post.getlist('price_unit[]') if hasattr(post, 'getlist') else post.get('price_unit[]', '').split(
            ',')

        if not customer_id or not product_ids or not quantities or not price_units:
            return request.redirect('/my/order/create?error=Missing+data')
        try:
            sale_order_lines = []
            for product_id, qty, price_unit in zip(product_ids, quantities, price_units):
                sale_order_lines.append((0, 0, {
                    'product_id': int(product_id),
                    'product_uom_qty': float(qty),
                    'price_unit': float(price_unit),
                }))
            # Get the current user (logged-in user)
            user_id = request.env.user.id
            default_user = request.env['res.users'].sudo().search([('id', '=', user_id)],limit=1)
            sale_order = request.env['sale.order'].sudo().create({
                'partner_id': int(customer_id),
                'user_id': default_user.id,  # Assign the user_id
                'state': "sale",
                'order_line': sale_order_lines,
            })

            return request.redirect('/my/orders')
        except Exception as e:
            return request.redirect('/my/order/create?error=%s' % str(e))