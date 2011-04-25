# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#SEE LICENSE file

#Python imports
from datetime import datetime

#Django imports
from django.core import mail
from django.test import TestCase

#App imports
from models import TestEmail

class TestEmailTestCase(TestCase):
	def setUp(self):
		self.te = TestEmail(
			date = datetime.now(),
			from_email = 'foo@example.com',
			to = 'bar@example.com',
			bcc = ''
		)
		
	
	def test_send(self):
		self.assertEquals(len(mail.outbox), 0)
		
		self.te.send()
		
		self.assertEquals(len(mail.outbox), 1)
		
	
	
	def test_test_email_save_handler(self):
		self.assertEquals(len(mail.outbox), 0)
		
		self.te.save()
		
		self.assertEquals(len(mail.outbox), 1)
		
