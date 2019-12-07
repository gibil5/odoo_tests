from django.db import models

from django.utils import timezone

# Create your models here.



class Sale(models.Model):
	"""
	Sale
	"""

	class Meta:

		ordering = ('date',)

		#verbose_name = 'Menu'
		#verbose_name_plural = 'Menus'


	
	name = models.CharField(
		#verbose_name='nombre',
		max_length=200,
	)


	date = models.DateTimeField(
		#verbose_name='fecha',
		default=timezone.now
	)


	state = models.CharField(
		#verbose_name='nombre',
		max_length=200,
	)




	total = models.DecimalField(
		#'total',
		max_digits=6, 
		decimal_places=2,
		default=0,
	)


	patient = models.CharField(
		#verbose_name='nombre',
		max_length=200,
		blank=True
	)


	x_type = models.CharField(
		#verbose_name='nombre',
		max_length=200,
		blank=True
	)



	serial_number = models.CharField(
		#verbose_name='nombre',
		max_length=200,
		blank=True
	)




