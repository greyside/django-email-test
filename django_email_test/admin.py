# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#SEE LICENSE file

#Python imports

#Django imports
from django.contrib import admin

#App imports
from models import TestEmail

class TestEmailAdmin(admin.ModelAdmin):
	list_display = ['subject', 'added', 'date', 'sent', 'error']
	list_filter = ['sent']
	readonly_fields = ['added', 'sent', 'error']
	save_as = True
	search_fields = ['subject', 'from_email', 'to', 'bcc', 'body', 'error']
	
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'to':
			request = kwargs.get('request', None)
			
			if request is not None:
				db_field.default = request.user.email
		
		return super(TestEmailAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(TestEmail, TestEmailAdmin)
