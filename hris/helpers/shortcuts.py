from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, _get_queryset
from django.template.defaultfilters import slugify, striptags, truncatewords as truncate_words

__all__ = [
  'reverse_redirect', 'reverse',
  'get_object_or_None', 'get_object_or_404',
  'send_mail', 'email_groups', 'email_staff', 'email_superusers',
  'slugify', 'striptags', 'truncate_words',
]

from_address = getattr(settings, 'DEFAULT_FROM_EMAIL', "webmaster@backscratch.com")

def reverse_redirect(url, args=[]):
    try:
        rev = reverse(url, args=args)
    except Exception, e:
        return HttpResponse('Unable to redirect: {0}'.format(e))
    else:
        return redirect(rev)
        
        
def get_object_or_None(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist, queryset.model.MultiplObjectsReturned:
        return None


def send_mail(recipients, subject, message, fail_silently=False):
    if subject and message and recipients:
        msg = EmailMultiAlternatives(subject, striptags(message), from_address, recipients)
        msg.attach_alternative(message, "text/html")
        msg.send()
        #print "Email", subject, "sent to", recipients
        #print message
    else:
        raise ValueError("Expects recipients, subject, message and  to be specified")
        

def email_groups(groups, subject, message, fail_silently=False):
    if subject and message:
        emails = User.objects.filter(groups__name__in=groups).exclude(email='')
        emails = emails.values_list('email', flat=True)
        send_mail(subject, message, emails)
    else:
        raise ValueError("Expects group, subject and message")


def email_staff(subject, message, fail_silently=False):
    if subject and message:
        emails = User.objects.filter(is_staff=True).exclude(email='')
        emails = emails.values_list('email', flat=True)
        send_mail(subject, message, emails)
    else:
        raise ValueError("Expects subject and message")
        
        
def email_superusers(subject, message, fail_silently=False):
    if subject and message:
        emails = User.objects.filter(is_superuser=True).exclude(email='')
        emails = emails.values_list('email', flat=True)
        send_mail(subject, message, emails)
    else:
        raise ValueError("Expects subject and message")
    
    
    

