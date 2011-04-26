# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#SEE LICENSE file

#Python imports
from datetime import datetime
import logging
import traceback

#Django imports
from django.conf import settings
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save

logger = logging.getLogger(__name__)

# Create your models here.

class TestEmail(models.Model):
	"""
	A model representing an email. Once created, the data in this model is used
	to send an email to the specified recipients, and any errors will be stored
	on the model.
	"""
	added = models.DateTimeField(auto_now_add=True)
	
	#email fields
	date = models.DateTimeField(
		default=lambda: datetime.now(),
		help_text="The date you want to set as the date header."
	)
	from_email = models.EmailField(
		'from',
		default=lambda: settings.DEFAULT_FROM_EMAIL
	)
	to = models.TextField(
		default='',
		#null=True,
		blank=True
	)
	bcc = models.TextField(
		default='',
		#null=True,
		blank=True
	)
	subject = models.CharField(
		max_length=150,
		default="This is a test email."
	)
	body = models.TextField(default="Here's some default text.")
	
	sent = models.BooleanField(default=False, editable=False)
	error = models.TextField(
		default='',
		blank=True,
		editable=False
	)
	
	def send(self):
		to = self.to.split(',')
		bcc = self.bcc.split(',')
		
		try:
			email = EmailMessage(self.subject, self.body, self.from_email, to, bcc)
			email.send()
			self.sent = True
		except Exception as e:
			logger.error(e)
			tb = traceback.format_exc()
			self.error = unicode(tb)
		
		#only save here if already in the database, otherwise the save_handler will call this function again
		if self.id:
			self.save()
	
	def __unicode__(self):
		return self.subject
	
	class Meta:
		ordering = ['-added']

def test_email_save_handler(sender, instance, created, **kwargs):
	if created:
		instance.send()
post_save.connect(test_email_save_handler, sender=TestEmail)

