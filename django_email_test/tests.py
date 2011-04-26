# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#SEE LICENSE file

#Python imports
from datetime import datetime

#Django imports
from django.core import mail
from django.core.mail import EmailMessage
from django.test import TestCase

#App imports
from models import TestEmail

class TestEmailTestCase(TestCase):
	def setUp(self):
		self.te = TestEmail(
			date = datetime.now(),
			from_email = 'foo@example.com',
			to = 'bar@example.com'
		)
		
	
	def test_send_success(self):
		self.assertEquals(len(mail.outbox), 0)
		self.assertEquals(self.te.sent, False)
		self.assertEquals(self.te.error, '')
		self.assertEquals(self.te.id, None)
		
		self.te.send()
		
		self.assertEquals(len(mail.outbox), 1)
		self.assertEquals(self.te.sent, True)
		self.assertEquals(self.te.error, '')
		self.assertEquals(self.te.id, None)
	
	def test_send_error(self):
		#TODO: move this to setUp() so that failures here don't affect other tests
		#need EmailMessage.send() (which is called in TestEmail.send() to throw an error)
		old_send = EmailMessage.send
		error = Exception('an error occurred!')
		def send_gives_error(*args, **kwargs):
			raise error
		EmailMessage.send = send_gives_error
		
		self.assertEquals(len(mail.outbox), 0)
		self.assertEquals(self.te.sent, False)
		self.assertEquals(self.te.error, '')
		self.assertEquals(self.te.id, None)
		
		self.te.send()
		
		self.assertEquals(len(mail.outbox), 0)
		self.assertEquals(self.te.sent, False)
		self.assertTrue(unicode(error) in self.te.error)
		self.assertEquals(self.te.id, None)
		
		#restore the original method so other tests can pass
		EmailMessage.send = old_send
	
	def test_test_email_save_handler_success(self):
		self.assertEquals(len(mail.outbox), 0)
		self.assertEquals(self.te.sent, False)
		self.assertEquals(self.te.error, '')
		self.assertEquals(self.te.id, None)
		
		self.te.save()
		
		#get object from DB to ensure 'sent' and 'error' were saved
		te = TestEmail.objects.all()[0]
		
		self.assertEquals(len(mail.outbox), 1)
		self.assertEquals(te.sent, True)
		self.assertEquals(te.error, '')
		self.assertNotEquals(te.id, None)
	
	def test_send_error(self):
		#need EmailMessage.send() (which is called in TestEmail.send() to throw an error)
		old_send = EmailMessage.send
		error = Exception('an error occurred!')
		def send_gives_error(*args, **kwargs):
			raise error
		EmailMessage.send = send_gives_error
		
		self.assertEquals(len(mail.outbox), 0)
		self.assertEquals(self.te.sent, False)
		self.assertEquals(self.te.error, '')
		self.assertEquals(self.te.id, None)
		
		self.te.save()
		
		#get object from DB to ensure 'sent' and 'error' were saved
		te = TestEmail.objects.all()[0]
		
		self.assertEquals(len(mail.outbox), 0)
		self.assertEquals(te.sent, False)
		self.assertTrue(unicode(error) in self.te.error)
		self.assertNotEquals(te.id, None)
		
		#restore the original method so other tests can pass
		EmailMessage.send = old_send
	
