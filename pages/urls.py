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

	#path('test_mgt', views.test_mgt, name='test_mgt'),
	path('test_mgt_repo/<int:repo_id>', views.test_mgt_repo, name='test_mgt_repo'),
]
