# -*- coding: utf-8 -*-
# from odoo import http


# class Recursos-humanos(http.Controller):
#     @http.route('/recursos-humanos/recursos-humanos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recursos-humanos/recursos-humanos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('recursos-humanos.listing', {
#             'root': '/recursos-humanos/recursos-humanos',
#             'objects': http.request.env['recursos-humanos.recursos-humanos'].search([]),
#         })

#     @http.route('/recursos-humanos/recursos-humanos/objects/<model("recursos-humanos.recursos-humanos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recursos-humanos.object', {
#             'object': obj
#         })

