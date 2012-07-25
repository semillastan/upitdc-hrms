from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from core.views import *

urlpatterns = patterns('',
    url(r'^tax_calculator', tax_calculator, name="tax-calc"), 
)
