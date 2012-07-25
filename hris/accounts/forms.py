from django import forms
from accounts.models import UserProfile, ContactInformation
from registration.forms import RegistrationFormUniqueEmail
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

year  = date.today().year
YEARS = range(year-16, year-100, -1) # only let people aged 18-100 register. :D

class RegistrationForm(RegistrationFormUniqueEmail):
    #first_name = forms.CharField(max_length=30, required=False)
    #last_name  = forms.CharField(max_length=30, required=False)
    #birthday = forms.DateField(widget=SelectDateWidget(years=YEARS), required=False)
    
    class Meta:
        fields  = ['username', 'email', 'password1', 'password2']
        

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name  = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    class Meta:
        model   = UserProfile
        fields  = ('first_name', 'last_name', 'email' ,'birthday', 'gender', 'city', 'country', 'bio', 'image', 'marital_status','personnel_id','designation','official_email')
        widgets = {'birthday': SelectDateWidget(years=YEARS)}
        
        
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].label = "About Me"
        for key in ['birthday', 'city', 'country']:
            self.fields[key].required = True
        
    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super(EditProfileForm, self).save()
        profile.user.first_name = self.cleaned_data['first_name']
        profile.user.last_name  = self.cleaned_data['last_name']
        profile.user.email  = self.cleaned_data['email']
        profile.user.save()
        return profile

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ('type', 'value')
        
ContactFormset = inlineformset_factory(User, ContactInformation, extra=1, max_num=10, form=ContactForm)
