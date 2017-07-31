# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Entry(models.Model):
    _name = 'automation.entry'

    name = fields.Char(required=True)
    email = fields.Text()
    phone = fields.Integer()
    city = fields.Char()

    @api.model
    def store_js_data_in_entry(self,user_details):
        # print user_details
        if user_details[0] != "":
            self.env['automation.entry'].create({
                'name':user_details[0],
                'email':user_details[1],
                'phone':user_details[2],
                'city':user_details[3],
            })
        else:
            print "values are blank"


        # for obj_out in user_details:
        # name = fields.Char(required=True,default=user_details[0])
        # email = fields.Text(default=user_details[1])
        # phone = fields.Integer(required=True,default=user_details[2])
        # city = fields.Char(required=True,default=user_details[3])            
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100