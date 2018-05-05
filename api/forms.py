from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    email = forms.CharField(
        required=True, help_text="@ucsc.edu email address required.", max_length=100)

    password = forms.CharField(required=True)

    confirm_password = forms.CharField(label="Confirm password", required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password', )

class LoginForm(forms.Form):
    email = forms.CharField(
        required=True, help_text="Email address required.", max_length=100)

    password = forms.CharField(required=True)