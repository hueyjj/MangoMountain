from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm


@csrf_exempt
def signup(request):
    print("signup: Request received")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            User.objects.create_user(
                username=email,
                email=email,
                password=password,
            ).save()
            return HttpResponse("Valid form received")
        else:
            return HttpResponse("Invalid form received")

    return HttpResponse("Request received")


@csrf_exempt
def login_user(request):
    if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           email = form.cleaned_data["email"]
           password = form.cleaned_data["password"]

           user = authenticate(request, username=email, password=password)
           if user:
               login(request, user)
               return HttpResponse("Login success")

           return HttpResponse("No user found")
       # TODO Log user automatically if user has valid session
       else:
           return HttpResponse(form.errors)
           #return HttpResponse("Invalid form")

    return HttpResponse("Invalid login")


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse("Logout successful")
    return HttpResponse("Require POST request to logout")
