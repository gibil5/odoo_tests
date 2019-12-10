# -*- coding: utf-8 -*-
"""
	Pages - Models

	Created: 			7 Dec 2019
	Last up: 	 		Id.
"""

from django.db import models
from django.utils import timezone

# Create your models here.






# ------------------------------------------------ Models ---------------------
class OdooModel(models.Model):
	"""
	Odoo Model
	"""

	class Meta:
		ordering = ('date',)



	name = models.CharField(
		max_length=200,
	)



	date = models.DateTimeField(
		default=timezone.now
	)



	date_begin = models.DateTimeField(
		default=timezone.now
	)

	date_end = models.DateTimeField(
		default=timezone.now
	)

	date_test = models.DateTimeField(
		default=timezone.now
	)






	state = models.CharField(
		max_length=200,
	)


	state_value = models.IntegerField(
		default=0,
	)



	content_value = models.DecimalField(
		max_digits=10, 
		decimal_places=2,
		default=0,
	)



	total = models.DecimalField(
		max_digits=10, 
		decimal_places=2,
		default=0,
	)



	count = models.IntegerField(
		default=0,
	)




	patient = models.CharField(
		max_length=200,
		blank=True
	)



	# Repo
	date_update = models.DateTimeField(
		default=timezone.now
	)

	configurator = models.CharField(
		max_length=200,
		blank=True
	)



	def __str__(self):
		return self.name




# Sale
class Sale(OdooModel):

	"""
	Sale
	"""

	class Meta:
		ordering = ('date',)


	serial_number = models.CharField(
		max_length=200,
		blank=True
	)

	x_type = models.CharField(
		max_length=200,
		blank=True
	)




# Management
class Management(OdooModel):

	"""
	Management
	"""

	class Meta:
		ordering = ('-date',)




# RSP
class ReportSaleProduct(OdooModel):
	"""
	RSP
	"""
	class Meta:
		ordering = ('-date_begin',)





# Marketing
class Marketing(OdooModel):

	"""
	Marketing
	"""

	class Meta:
		ordering = ('-date',)







# Host
class Host(models.Model):

	"""
	Host
	"""

	class Meta:
		ordering = ('name',)


	name = models.CharField(
		max_length=200,
	)



	hostname = models.CharField(
		max_length=200,
	)


	database = models.CharField(
		max_length=200,
	)


	login = models.CharField(
		max_length=200,
	)


	password = models.CharField(
		max_length=200,
	)








