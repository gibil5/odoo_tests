# -*- coding: utf-8 -*-
"""
	Lib

	Created: 			7 Dec 2019
	Last up: 	 		Id.
"""

import datetime
import odoolib
from .models import *
import sys




# ------------------------------------------------ Marketing ---------------------

# Update
def update_mkt_repos(connection, year, name):
	print()
	print('Test MKT')
	print()

	state_arr = []
	obj_array = []


	so_model = connection.get_model('openhealth.marketing')


	# Search
	if name in ['all']:	
		repo_ids = so_model.search([
										('year', '=', year),
										#('several_dates', '=', True),
									])
	else:
		repo_ids = so_model.search([
										('year', '=', year),
										('name', '=', name),
										#('several_dates', '=', True),
									])

	print(repo_ids)

	# Update
	for repo_id in repo_ids:

		# Tests
		out_0 = 0 


		# Fast
		print('Test - Update')
		out_0 = so_model.update(repo_id)
		print(out_0)



		# Total
		state_value = out_0
		print()
		print(state_value)

		if state_value == 1:
			print('Stable')
			state = 'stable'

		else:
			print('Unstable')
			state = 'unstable'


		# Set State
		so_model.set_state(repo_id, state)

		state_arr.append(state)



# Create Django Obj

		# Variables
		name = so_model.get_name(repo_id)
		date_begin = so_model.get_date_begin(repo_id)
		date_end = so_model.get_date_end(repo_id)

		date_test = get_date_corrected(so_model.get_date_test(repo_id))

		#total = so_model.get_total(repo_id)
		count = so_model.get_count(repo_id)

		state = so_model.get_state(repo_id)

		#configurator = so_model.get_configurator(repo_id)


		print()
		print()
		print(name)
		print(date_begin)
		print(date_end)
		print(date_test)

		#print(total)
		print(count)

		print(state)

		# Create 
		obj = Marketing(name=name, 
								date_begin=date_begin, 
								date_end=date_end,
								date_test=date_test,

								#total=total,
								count=count,

								state=state, 
		) 	

		obj.save()

		print(obj)
		print()
		print()
		print()
		
		obj_array.append(obj)


	return state_arr, obj_array




# ------------------------------------------------ RSP ---------------------

# Update
def update_rsp_repos(connection, year, name):
	print()
	print('Test RSP')
	print()

	state_arr = []
	obj_array = []

	so_model = connection.get_model('openhealth.report.sale.product')


	# Search
	if name in ['all']:	
		repo_ids = so_model.search([
										#('year', '=', year),
										('several_dates', '=', True),
									])
	else:
		repo_ids = so_model.search([
										#('year', '=', year),
										('name', '=', name),
										('several_dates', '=', True),
									])

	print(repo_ids)

	# Update
	for repo_id in repo_ids:

		# Tests
		out_0 = 0 

		# Fast
		print('Test - Update')
		out_0 = so_model.update(repo_id)
		print(out_0)


		# Total
		state_value = out_0
		print()
		print(state_value)

		if state_value == 1:
			print('Stable')
			state = 'stable'

		else:
			print('Unstable')
			state = 'unstable'

		# Set State
		so_model.set_state(repo_id, state)

		state_arr.append(state)



# Create Django Obj

		# Variables
		name = so_model.get_name(repo_id)
		date_begin = so_model.get_date_begin(repo_id)
		date_end = so_model.get_date_end(repo_id)

		date_test = get_date_corrected(so_model.get_date_test(repo_id))

		total = so_model.get_total(repo_id)
		count = so_model.get_count(repo_id)

		state = so_model.get_state(repo_id)

		#configurator = so_model.get_configurator(repo_id)


		print()
		print()
		print(name)
		print(date_begin)
		print(date_end)
		print(date_test)

		print(total)
		print(count)

		print(state)

		# Create 
		obj = ReportSaleProduct(name=name, 
								date_begin=date_begin, 
								date_end=date_end,
								date_test=date_test,

								total=total,
								count=count,

								state=state, 
		) 	

		obj.save()

		print(obj)
		print()
		print()
		print()
		
		obj_array.append(obj)


	return state_arr, obj_array





# ------------------------------------------------ Management ---------------------

# Get Managements
def get_management_repos(connection, year, name):
	print()
	print('Test Management')
	print()

	mgt_array = []

	so_model = connection.get_model('openhealth.management')


	# Search
	if name in ['all']:	
		repo_ids = so_model.search([
										('year', '=', year),
									])
	else:
		repo_ids = so_model.search([
										('year', '=', year),
										('name', '=', name),
									])

	#print(repo_ids)



	for repo_id in repo_ids:


# Test Odoo Obj

		out_0 = 0 
		out_1 = 0 
		out_2 = 0 
		out_3 = 0 
		out_4 = 0 


		# Fast
		print('Test - Fast')
		out_0 = so_model.update_fast(repo_id)
		print(out_0)

		# Patients
		print('Test - Patients')
		out_1 = so_model.update_patients(repo_id)
		print(out_1)

		# Doctors
		print('Test - Doctors')
		out_2 = so_model.update_doctors(repo_id)
		print(out_2)

		# Productivity
		print('Test - Productivity')
		out_3 = so_model.update_productivity(repo_id)
		print(out_3)


		# Daily
		#print('Test - Daily')
		#out_4 = so_model.update_daily(repo_id)
		#print(out_4)
		try:
			out_4 = so_model.update_daily(repo_id)
			print(out_4)


		except odoolib.main.JsonRPCException:
			print('Lib - Exception')

			etype, eval, etb = sys.exc_info()
			
			print(etype)
			print()
			print(eval)
			print()
			#print(etb)
			#print()

			#print(eval.message)
			#print(eval['message'])
			#print(eval['code'])
			#print(eval['data'])
			print()

		except:
			print("Something else went wrong")
			print()





		# Total
		state_value = out_0 + out_1 + out_2 + out_3 + out_4
		print()
		print(state_value)

		if state_value == 5:
			print('Stable')
			state = 'stable'
		else:
			print('Unstable')
			state = 'unstable'

		# Set State
		so_model.set_state(repo_id, state)



		# Test content
		out_0, out_1 = so_model.validate(repo_id)
		content_value = out_0 + out_1
		print(out_0)
		print(out_1)
		print(content_value)


# Create Django Obj

		# Variables
		name = so_model.get_name(repo_id)
		date = so_model.get_date(repo_id)
		date_update = get_date_corrected(so_model.get_date_update(repo_id))
		total = so_model.get_total(repo_id)
		configurator = so_model.get_configurator(repo_id)
		state = so_model.get_state(repo_id)

		print()
		print()
		print(name)
		print(date)
		print(date_update)
		print(total)
		print(configurator)
		print(state)

		# Create 
		mgt = Management(name=name, 
							date=date, 
							date_update=date_update,
							total=total,
							configurator=configurator,
							state=state, 
							state_value=state_value, 
							content_value=content_value, 
		) 	

		mgt.save()

		print(mgt)
		print()
		print()
		print()
		
		mgt_array.append(mgt)

	return mgt_array



# Get Sales
def get_sales(connection, partner_id):
	print()
	print('Get Partner')

	sale_array = []

	so_model = connection.get_model('sale.order')

	sale_ids = so_model.search([('partner_id', '=', partner_id)])

	# Loop
	for sale_id in sale_ids:

		# Functions
		test = so_model.test_serial_number(sale_id)

		# Variables
		name = so_model.get_name(sale_id)
		date = so_model.get_date(sale_id)
		state = so_model.get_state(sale_id)

		total = so_model.get_total(sale_id)
		patient = so_model.get_patient(sale_id)
		x_type = so_model.get_type(sale_id)

		serial_number = so_model.get_serial_number(sale_id)

		print()
		print(name)
		print(date)
		print(state)

		sale = Sale(name=name, date=date, state=state, total=total, patient=patient, x_type=x_type, serial_number=serial_number)
		sale.save()
		print(sale)

		sale_array.append(sale)


	print()
	print(sale_ids)
	print(len(sale_ids))
	print()

	#return sale_ids, so_model
	return sale_array




def get_partner(connection, name):
	print()
	print('Get Partner')

	partner_model = connection.get_model('res.partner')

	#jr_id = partner_model.search([('name', '=', 'REVILLA RONDON JOSE JAVIER')])[0]
	partner_id = partner_model.search([('name', '=', name)])[0]

	return partner_id





# ----------------------------------------------------------- Connect ---------------------------------

# Connect
#def connect():
#def connect(hostname, database):
#def connect(hostname, database, login, password):
def connect(name):
	print()
	print('Connect')


	host = Host.objects.filter(name=name)[0]
	#print(host)

	hostname = host.hostname
	database = host.database
	login = host.login
	password = host.password

	#print(hostname)


	# Connect - Json Rpc
	connection = odoolib.get_connection(
											#hostname='localhost',
											#login="jrevilla55@gmail.com",
											#database="ODOO-TACNA",
											#password="nyctal6+",

											hostname=hostname,
											database=database,											
											login=login,
											password=password,

											port=8069,
											protocol='jsonrpc',
									)
	#print()
	#print(connection)

	return connection




# ----------------------------------------------------------- Aux ---------------------------------
def get_date_corrected(date_order):
	"""
	Used by:
		- Get Ticket Raw
	"""
	#print()
	#print('Get Date Corrected')
	#print(date_order)

	#print()
	#print('mark 1')

	DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	#DATETIME_FORMAT = "%d-%m-%y- %H:%M:%S"

	date_field1 = datetime.datetime.strptime(date_order, DATETIME_FORMAT)
	#print(date_field1)


	#print()
	#print('mark 2')

	date_field2 = date_field1 + datetime.timedelta(hours=-5, minutes=0)
	#print(date_field2)
	

	#DATETIME_FORMAT_2 = "%d-%m-%Y %H:%M:%S"

	#print()
	#print('mark 3')

	#date_corrected = date_field2.strftime(DATETIME_FORMAT_2)
	date_corrected = date_field2.strftime(DATETIME_FORMAT)
	#print(date_corrected)

	#print()
	#print('mark 4')
	return date_corrected
