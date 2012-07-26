from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from imagekit.models import ImageModel
import os, datetime

GENDER = (
    (u'Male', u'Male'),
    (u'Female', u'Female'),
)

MARITAL_STATUS = (
	(u'Single', u'Single'),
	(u'Married', u'Married'),
	(u'Widowed', u'Widowed'),
)

def upload_to(instance, filename):
    name, dot, ext = filename.rpartition('.')
    name = "{0}.{1}".format(instance.user.username, ext)
    return os.path.join('profiles', name)

class Department(models.Model):
	name = models.CharField("Department", max_length=120)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	last_updated = models.DateTimeField(default=datetime.datetime.now())
	
	def save(self, *args, **kwargs):
		self.last_updated = datetime.datetime.now()
		super(Department, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name

class Designation(models.Model):
	name = models.CharField("Designation", max_length=120)
	department = models.ForeignKey(Department, verbose_name="Department")
	
	created = models.DateTimeField(default=datetime.datetime.now())
	last_updated = models.DateTimeField(default=datetime.datetime.now())
	
	def save(self, *args, **kwargs):
		self.last_updated = datetime.datetime.now()
		super(Designation, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class UserProfile(ImageModel):
    user  = models.OneToOneField(User, verbose_name="User")
    bio   = models.TextField("About Me", blank=True, null=True)
    image = models.ImageField("Photo", upload_to=upload_to, storage=settings.UPLOAD_STORAGE, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(verbose_name="Gender", max_length=6, choices=GENDER, blank=True, null=True)
    marital_status = models.CharField(verbose_name="Marital Status", max_length=20, choices=MARITAL_STATUS, blank=True, null=True)
    
    # better a foreign key to some predefined lists
    city = models.CharField("City", max_length=30, blank=True, null=True)    
    country = models.CharField("Country", max_length=30, blank=True, null=True, default="Philippines")
    
    personnel_id = models.PositiveIntegerField(default=0, blank=True, null=True)
    designation = models.ForeignKey(Designation, blank=True, null=True)
    official_email = models.EmailField(blank=True, null=True)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    class IKOptions:
        spec_module = 'core.specs'
        image_field = 'image'    
        cache_dir   = 'cache'
    
    def __unicode__(self):
        return u"{0}'s profile".format(self.user.username)

    @property
    def fullname(self):
        return self.user.get_full_name()
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    
    @property
    def location(self):
        if self.city and self.country:
            return "{0}, {1}".format(self.city, self.country)
        else:
            return None

CONTACT_TYPE = (
    (u'Email Address',u'Email Address'),
    (u'Landline',u'Landline'),
    (u'Mobile Number',u'Mobile Number'),
    (u'Fax',u'Fax'),
)

class ContactInformation(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    value = models.CharField("Value", max_length=120)
    type = models.CharField("Type", max_length=50, choices=CONTACT_TYPE)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Contract(models.Model):
	user = models.ForeignKey(User, verbose_name="User Contract", related_name="user_contract")
	start = models.DateField()
	end = models.DateField(blank=True, null=True)
	salary_per_hour = models.PositiveIntegerField(default=0)
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created By", related_name="user_contract_created")
	last_updated = models.DateTimeField(blank=True, null=True)
	is_active = models.BooleanField(default=True)
	
	@property
	def salary_per_day(self):
		return self.salary_per_hour * 8
		
	@property
	def salary_per_month(self):
		return self.salary_per_hour * 176
		
	def save(self, *args, **kwargs):
		self.last_updated = datetime.datetime.now()
		super(Contract, self).save(*args, **kwargs)
