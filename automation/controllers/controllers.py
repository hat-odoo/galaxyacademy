# -*- coding: utf-8 -*-
from odoo import http

class Automation(http.Controller):
    @http.route('/automation/automation/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/automation/automation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('automation.listing', {
#             'root': '/automation/automation',
#             'objects': http.request.env['automation.automation'].search([]),
#         })

#     @http.route('/automation/automation/objects/<model("automation.automation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automation.object', {
#             'object': obj
#         })