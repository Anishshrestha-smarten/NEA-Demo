# -*- coding: utf-8 -*-
# from odoo import http


# class Neafsm(http.Controller):
#     @http.route('/neafsm/neafsm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/neafsm/neafsm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('neafsm.listing', {
#             'root': '/neafsm/neafsm',
#             'objects': http.request.env['neafsm.neafsm'].search([]),
#         })

#     @http.route('/neafsm/neafsm/objects/<model("neafsm.neafsm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('neafsm.object', {
#             'object': obj
#         })
