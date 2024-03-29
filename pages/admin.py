# -*- coding: utf-8 -*-
"""
	Pages - Admin

	Created: 			7 Dec 2019
	Last up: 	 		Id.
"""

from django.contrib import admin

# Register your models here.

from .models import *


class SaleAdmin(admin.ModelAdmin):

	list_display = ('name', 'serial_number', 'date', 'x_type', 'patient', 'state', 'total', )

	list_display_links = ('name', 'serial_number', )

	list_filter = ('state', 'x_type', )

	#list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25



class ManagementAdmin(admin.ModelAdmin):

	list_display = ('name', 'date_update', 'date', 'state', 'total', )

	list_display_links = ('name', )

	list_filter = ('state', )

	#list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25



class ReportSaleProductAdmin(admin.ModelAdmin):

	list_display = ('name', 'date_begin', 'date_end', 'date_test', 'state', 'total', 'count', )

	list_display_links = ('name', )

	list_filter = ('state', )

	#list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25




class MarketingAdmin(admin.ModelAdmin):

	list_display = ('name', 'date_begin', 'date_end', 'date_test', 'state', 'total', 'count', )

	list_display_links = ('name', )

	list_filter = ('state', )

	#list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25







class HostAdmin(admin.ModelAdmin):

	list_display = ('name', 'hostname', 'database', 'login', 'password', )

	list_display_links = ('name', )

	#list_filter = ('state', 'x_type', )

	#list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25




admin.site.register(Sale, SaleAdmin)

admin.site.register(Management, ManagementAdmin)

admin.site.register(ReportSaleProduct, ReportSaleProductAdmin)

admin.site.register(Marketing, MarketingAdmin)


admin.site.register(Host, HostAdmin)



