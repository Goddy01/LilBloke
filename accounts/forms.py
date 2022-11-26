from django import forms
from .models import UserAccount

class SignInForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'password1', 'password2']