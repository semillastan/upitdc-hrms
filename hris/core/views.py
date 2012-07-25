from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from helpers import *
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime

from accounts.models import *
from core.models import *
from core.forms import *

@render_to('core/add-tax-table.html')
def add_tax_table(request):
	form = TaxTableForm()
	if request.method == 'POST':
		form = TaxTableForm(data=request.POST)
		if form.is_valid():
			form.save()
	return {'form':form}

@render_to('tax_calculator.html')
def tax_calculator(request):
	return {'date':datetime.datetime.now()}
