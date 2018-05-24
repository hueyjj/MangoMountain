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

class CourseForm(forms.Form):
    term = forms.CharField()
    status = forms.CharField()
    subject = forms.CharField()
    course_num = forms.IntegerField()
    course_title_key_word = forms.CharField()
    instructor_last_name = forms.CharField()
    general_education = forms.CharField()
    course_units = forms.CharField()
    meeting_days = forms.CharField()
    course_career = forms.CharField()
