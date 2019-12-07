# -*- coding: utf-8 -*-
"""
	Pages - Views

	Created:	 3 Dec 2019
	Last up:	 3 Dec 2019
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Sale, Management
from . import lib

# Create your views here.



# ------------------------------------------------ Test Management ---------------------
def test_mgt(request):
	print()
	print('Test Report Mgt')

	# Connect
	lib.connect()


	# Clean
	Management.objects.all().delete()


	# Connect
	connection = lib.connect()


	# Reports
	year = '2019'
	#year = '2018'
	repos = lib.get_management_repos(connection, year)
	print(repos)


	ctx = {
			'repos': repos,

	}

	output = render(request, 'pages/test_mgt.html', ctx)

	return HttpResponse(output)




# ------------------------------------------------ Test Sales ---------------------
def test_sales(request):
	print()
	print('Test Sales')


	# Clean
	Sale.objects.all().delete()


	# Connect
	connection = lib.connect()



	# Partners
	#name = 'REVILLA RONDON JOSE JAVIER'
	name = 'PATIÑO PATIÑO NIÑA CLARA'
	partner_id = lib.get_partner(connection, name)


	# Sales
	#sale_ids, so_model = lib.get_sales(connection, partner_id)
	sales = lib.get_sales(connection, partner_id)
	print(sales)


	ctx = {
			'sales': sales,

	}

	output = render(request, 'pages/test_sales.html', ctx)

	return HttpResponse(output)



# ------------------------------------------------ Home ---------------------

def home(request):

	ctx = {}

	output = render(request, 'pages/home.html', ctx)

	return HttpResponse(output)

