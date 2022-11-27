from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail
from .models import UserAccount
from django.https import HttpResponse

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('accounts/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = signup_form.cleaned_data.get('email')
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, to_email, fail_silently=True)
            return redirect('activation_sent')
    else:
        singup_form = forms.SignUpForm()
    return render(request, 'accounts/signup.html')

def sign_in(request):
    return render(request, 'accounts/signin.html')

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserAccount.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Success')
    else:
        return render(request, 'accounts/activation_invalid.html')