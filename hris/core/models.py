from django.db import models
from django.contrib.auth.models import User
from accounts.models import *
import datetime

TAX_STATUS = (
	(u'Z',u'Z'),
	(u'S/ME',u'S/ME'),
	(u'ME1/SE1',u'ME1/S1'),
	(u'ME2/SE2',u'ME2/S2'),
	(u'ME3/SE3',u'ME3/S3'),
	(u'ME4/SE4',u'ME4/S4'),
)

class TaxTable(models.Model):
	status = models.CharField(max_length=20, choices=TAX_STATUS, unique=True)
	bracket = models.PositiveIntegerField(default=0)
	
	exemption = models.PositiveIntegerField(default=0)
	over = models.PositiveIntegerField(default=0)
	max_amount = models.PositiveIntegerField(default=0)
	min_amount = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return u'{0} - {1}'.format(self.status, self.bracket)

class PaySlip(models.Model):
	user = models.ForeignKey(User, verbose_name="User")
	start = models.DateField(blank=True, null=True)
	end = models.DateField(blank=True, null=True)
	
	salary_per_day = models.PositiveIntegerField(default=0)
	working_days = models.PositiveIntegerField(default=0, verbose_name="No. of Working Days")
	
	# Add Monthly Allowances & Incentives
	transportation = models.PositiveIntegerField(default=0, verbose_name="Transportation")
	communication = models.PositiveIntegerField(default=0, verbose_name="Communication")
	project_honoraria = models.PositiveIntegerField(default=0, verbose_name="Other Project Honoraria")
	project_incentive = models.PositiveIntegerField(default=0, verbose_name="Project Incentive")
	
	# Deductions
	sss = models.PositiveIntegerField(default=0, verbose_name="SSS")
	philhealth = models.PositiveIntegerField(default=0, verbose_name="PhilHealth")
	pagibig = models.PositiveIntegerField(default=0, verbose_name="Pag-Ibig Fund")
	withholding_tax = models.PositiveIntegerField(default=0, verbose_name="Withholding Tax")
	loan = models.PositiveIntegerField(default=0, verbose_name="Loan")
	others = models.PositiveIntegerField(default=0, verbose_name="Others")
	
	created = models.DateTimeField(datetime.datetime.now())
	created_by = models.ForeignKey(User, related_name="payslip_created_by")

	@property
	def monthly_salary(self):
		return self.salary_per_day * 22
	
	@property
	def gross_salary_for_period(self):
		return self.salary_per_day * self.working_days
		
	@property
	def total_gross_salary(self):
		total = self.transportation + self.communication + self.project_honoraria + self.project_incentive
		return self.gross_salary_for_period + total
	
	@property
	def total_deductions(self):
		total = self.sss + self.philhealth + self.pagibig + self.withholding_tax + self.loan + self.others
		return self.total_gross_salary - total

	def __unicode__(self):
		return u'{0}: {1} - {2}'.format(self.user, self.start, self.end)
