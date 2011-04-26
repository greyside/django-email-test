# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#SEE LICENSE file

#Python imports

#Django imports
from django.contrib import admin

#App imports
from models import TestEmail

class TestEmailAdmin(admin.ModelAdmin):
	readonly_fields = ['sent', 'error']
	save_as = True

admin.site.register(TestEmail, TestEmailAdmin)
