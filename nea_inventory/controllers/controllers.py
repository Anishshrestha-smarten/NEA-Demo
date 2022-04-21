# -*- coding: utf-8 -*-
# from odoo import http


# class NeaInventory(http.Controller):
#     @http.route('/nea_inventory/nea_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nea_inventory/nea_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nea_inventory.listing', {
#             'root': '/nea_inventory/nea_inventory',
#             'objects': http.request.env['nea_inventory.nea_inventory'].search([]),
#         })

#     @http.route('/nea_inventory/nea_inventory/objects/<model("nea_inventory.nea_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nea_inventory.object', {
#             'object': obj
#         })
