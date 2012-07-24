from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from registration import signals

from helpers import get_object_or_404, render_to, reverse_redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from accounts.forms import EditProfileForm, ContactFormset
from accounts.models import UserProfile
from django.core.mail import send_mail, EmailMessage
from datetime import date

@render_to('accounts/profile.html')
def profile(request, username=''):    
    mine = False
    if username == '':
        if request.user.is_authenticated():
            profile = request.user.get_profile()
            mine = True
        else:
            return reverse_redirect('home')
    else:
        user = get_object_or_404(User, username=username)
        profile = user.get_profile()
        me = UserProfile.objects.get(user=request.user)
        if user == request.user:
            mine = True
    
    return {'profile': profile, 'mine': mine}
    
    
@login_required
@render_to('accounts/edit-profile.html')
def edit_profile(request):
    
    #formset = ContactFormset(prefix="contact")
    profile = request.user.get_profile()
    initial = { 'first_name': profile.user.first_name, 'last_name': profile.user.last_name, 'email': profile.user.email }
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
           form.save()
           return reverse_redirect('profile')         
    else:
        form = EditProfileForm(initial=initial, instance=profile)
    return {'form': form}#, 'formset':formset}
    
def register_user(sender, user, request, **kwargs):
    ''' This will only be called when the registration form has validated 
        so we assume it is safe to utilize the POST parameters
    '''
    if request.method == 'POST':
        user.save()
        profile = user.get_profile()
        profile.save()

def update_user(sender, user, request, **kwargs):
    ''' This will only be called when the registration form has validated 
        so we assume it is safe to utilize the POST parameters
    '''
    if request.method == 'POST':    
        user.first_name = request.POST.get('first_name')
        user.last_name  = request.POST.get('last_name')
        user.save()
        
        y = request.POST.get('birthday_year')
        m = request.POST.get('birthday_month')
        d = request.POST.get('birthday_day')
        profile = user.get_profile()
        profile.birthday = date(int(y), int(m), int(d))
        profile.save()

signals.user_registered.connect(register_user, sender=None, weak=False, dispatch_uid="accounts_views_update_user")

@render_to('accounts/forgot_password.html')
def forgot_password(request):
    if request.method == 'POST':
        user = get_object_or_None(User, email=request.POST['email'])
        if user:
            code = '343aasd'
            subject = '[SemillaStan.com] Forgot Password'
            body = """Good day! \n\n We believe that you have asked to reset your password. Kindly proceed to http://semillastan.com/accounts/reset/password/ and enter this """ + code + """ to change your password."""
            e = []
            e.append(user.email)
            email = EmailMessage(subject, body, 'mail@semillastan.com', e)
            email.send(fail_silently=False)
    return {'forgot': True}
