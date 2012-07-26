from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from helpers import *
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime

from accounts.models import *
from accounts.forms import *
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

@render_to('core/departments.html')
def all_departments(request):
	return {'departments':Department.objects.all()}

@login_required
@render_to('core/add-department.html')
def add_department(request):
	if request.method == 'POST':
		form = DepartmentForm(data=request.POST)
		if form.is_valid():
			form.save()
	form = DepartmentForm()
	return {'form':form}

@login_required
def edit_department(request, department_id=None):
	department = get_object_or_None(Department, pk=department_id)
	context['department'] = department
	context['departments'] = Department.objects.all()
	template = "core/departments.html"
	if department:
		form = DepartmentForm(instance=department)
		template = "core/edit-department.html"
		if request.method == 'POST':
			form = DepartmentForm(data=request.POST, instance=department)
			template = "core/edit-department.html"
			if form.is_valid():
				form.save()
				template = "core/departments.html"
		context['form'] = form
	return render_to_response(template,context, context_instance=RequestContext(request))

@login_required
@render_to('core/departments.html')
def delete_department(request, department_id=None):
	profile = request.user.get_profile()
	if profile.department is 'Human Resource Department':
		department = get_object_or_None(Department, pk=department_id)
		if department:
			department.delete()
	return {'departments':Department.objects.all()}
