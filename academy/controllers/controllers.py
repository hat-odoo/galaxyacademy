# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):
	@http.route('/academy/academy/', auth='public',website=True)
	def index(self, **kw):
		# return "Hello, world"
		Teachers = http.request.env['academy.teachers']
		# print Teachers.search([])
		return http.request.render('academy.index', {
			'teachers': Teachers.search([]),
		})

	@http.route('/academy/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
	def teacher(self, teacher):
		return http.request.render('academy.biography', {
			'person': teacher
		})

	@http.route('/academy/course/',auth='public',website=True)
	def indexcourse(self,**kw):
		Courses = http.request.env['academy.courses']
		return http.request.render('academy.indexcourse', {
			'courses': Courses.search([]),
		})
	
	@http.route('/academy/course/<model("academy.courses"):course>/', auth='public', website=True)
	def course(self, course):
		return http.request.render('academy.teacher_id', {
			'person': course
		})



#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })