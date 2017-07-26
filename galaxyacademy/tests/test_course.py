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
        recordExam.write({'description':'s just sa'})
        recordSession.write({'attendee_ids':'Agrolait','seats':'10','attendees_count':'1'})
        # print recordSession
        recordSession.action_confirm()
        recordCourse.write({'session_ids':recordSession})
        # print recordCourse.session_ids

