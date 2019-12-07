"""
Pages - urls 

"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

	path('', views.home, name='home'),

	path('test_sales', views.test_sales, name='test_sales'),

	path('test_mgt', views.test_mgt, name='test_mgt'),
]
