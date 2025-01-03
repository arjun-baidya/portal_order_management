{
    "name": "Portal Order Management",
    "version": "17.0.0.0",
    "category": "Sales",
    "summary": "Enable portal users to place orders for others and view specific invoices.",
    "description": "This module extends the portal functionality to allow portal users to create sales orders for other customers and restrict their invoice visibility.",
    "author": "Arjun Baidya",
    "website": "https://yourwebsite.com",
    "depends": ["sale", "account", "website", "portal"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "views/invoice_views.xml",
        "views/portal_template.xml",
        "views/create_sale_order_template.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            '/portal_order_management/static/src/js/order_form.js',
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False
}
