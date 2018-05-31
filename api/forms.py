from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


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
    term = forms.CharField(required=False)
    status = forms.CharField(required=False)
    subject = forms.CharField(required=False)
    course_num = forms.IntegerField(required=False)
    course_title_key_word = forms.CharField(required=False)
    instructor_last_name = forms.CharField(required=False)
    general_education = forms.CharField(required=False)
    course_units = forms.CharField(required=False)
    meeting_days = forms.CharField(required=False)
    course_career = forms.CharField(required=False)

class CreateReviewForm(forms.Form):
    subject = forms.CharField(required=True)
    term = forms.CharField(required=True)
    course_title = forms.CharField(required=True)
    rating = forms.IntegerField(required=True)
    comment = forms.CharField(required=True)

class ReviewForm(forms.Form):
    search_term = forms.CharField(required=True)