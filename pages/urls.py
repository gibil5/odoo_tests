"""
Pages - urls 

"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

	path('', views.home, name='home'),


	# Test sites
	path('test_dev', views.test_dev, name='test_dev'),

	path('test_tacna', views.test_tacna, name='test_tacna'),

	path('test_lima', views.test_lima, name='test_lima'),



	# Sales
	path('test_sales', views.test_sales, name='test_sales'),


	# Management
	path('test_mgt', views.test_mgt, name='test_mgt'),
	#path('test_mgt_repo/<int:repo_id>', views.test_mgt_repo, name='test_mgt_repo'),
	path('test_mgt_repo/<slug:name>', views.test_mgt_repo, name='test_mgt_repo'),


	# RSP
	path('test_rsp_repo/<slug:name>', views.test_rsp_repo, name='test_rsp_repo'),


	# Marketing
	path('test_mkt_repo/<slug:name>', views.test_mkt_repo, name='test_mkt_repo'),

]

