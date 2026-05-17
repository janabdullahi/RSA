# -*- coding: utf-8 -*-
# from odoo import http


# class Resident(http.Controller):
#     @http.route('/resident/resident', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/resident/resident/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('resident.listing', {
#             'root': '/resident/resident',
#             'objects': http.request.env['resident.resident'].search([]),
#         })

#     @http.route('/resident/resident/objects/<model("resident.resident"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('resident.object', {
#             'object': obj
#         })

