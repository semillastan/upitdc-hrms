from django import forms
from accounts.models import UserProfile, ContactInformation
from registration.forms import RegistrationFormUniqueEmail
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from core.models import TaxTable, PaySlip
import datetime

year  = date.today().year
YEARS = range(year-100, -1)

class TaxTableForm(forms.ModelForm):	
	class Meta:
		model = TaxTable
		fields = ['status','bracket','exemption','over','max_amount','min_amount']
		
class PaySlipForm(forms.ModelForm):
	class Meta:
		model = PaySlip
		fields = ['user']

