from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from core.views import *

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template':'home.html'}),
    url(r'^tax-calc$', tax_calculator, name="tax-calc"),
    
    url(r'department/all', all_departments, name="all-departments"),
)
