# -*- coding: utf-8 -*-
from odoo import http

# class Galaxyacademy(http.Controller):
#     @http.route('/galaxyacademy/galaxyacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/galaxyacademy/galaxyacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('galaxyacademy.listing', {
#             'root': '/galaxyacademy/galaxyacademy',
#             'objects': http.request.env['galaxyacademy.galaxyacademy'].search([]),
#         })

#     @http.route('/galaxyacademy/galaxyacademy/objects/<model("galaxyacademy.galaxyacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('galaxyacademy.object', {
#             'object': obj
#         })