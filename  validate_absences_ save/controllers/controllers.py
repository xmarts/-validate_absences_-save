# -*- coding: utf-8 -*-
from odoo import http

# class PraticasM(http.Controller):
#     @http.route('/praticas_m/praticas_m/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/praticas_m/praticas_m/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('praticas_m.listing', {
#             'root': '/praticas_m/praticas_m',
#             'objects': http.request.env['praticas_m.praticas_m'].search([]),
#         })

#     @http.route('/praticas_m/praticas_m/objects/<model("praticas_m.praticas_m"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('praticas_m.object', {
#             'object': obj
#         })