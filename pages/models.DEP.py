"""
Pages - Models
"""

from django.db import models

from django.utils import timezone

# Create your models here.



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


	state = models.CharField(
		max_length=200,
	)




	total = models.DecimalField(
		max_digits=6, 
		decimal_places=2,
		default=0,
	)


	patient = models.CharField(
		max_length=200,
		blank=True
	)







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





