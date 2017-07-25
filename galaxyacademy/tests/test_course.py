from odoo.tests.common import TransactionCase

class TestSample(TransactionCase):
    at_install = False
    post_install = True
    def test_course(self):
    	recordCourse = self.env['galaxyacademy.course'].create({'name': 'Course_TestSample',
    		'exam_entry':'True'})
    	recordSession = self.env['galaxyacademy.session'].create({'name':'Session_TestSample'})
    	recordExam = self.env['galaxyacademy.exam'].create({'name':'Exam_TestSample',
    		'course_id':recordCourse.id})

    	# updateExam = self.env.ref('galaxyacademy.exam')
    	# updateExam.write({'description':'This is just sample, not to overwrite it.'})
    	self.env['galaxyacademy.exam'].write({'description':'s just sa'})
        # record.some_action()

        # self.assertEqual(
        #     record.field,
        #     expected_field_value)

    	# team = self.env['crm.team'].sudo(self.crm_salemanager.id).create({'name': "Phone Marketing"})
     #    lead = self.env.ref('crm.crm_case_1')
     #    lead.sudo(self.crm_salemanager.id).write({'team_id': team.id})
        # self.assertEqual(1, 0)

    # def test_session(self):
    # 	record = self.env['galaxyacademy.session'].create({'name':'Session_TestSample'})

    # def test_exam(self):
    # 	record = self.env['galaxyacademy.exam'].create({'name':'Exam_TestSample',
    # 		'course_id':'Course_TestSample'})