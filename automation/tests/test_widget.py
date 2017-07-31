from odoo.tests.common import TransactionCase

class TestSample(TransactionCase):
    at_install = False
    post_install = True
    def test_widget(self):
        recordEntry = self.env['automation.entry'].create({'name':'Exam_TestSample',
            'phone':'123456789'})
        recordEntry.write({'city':'s just sa'})
