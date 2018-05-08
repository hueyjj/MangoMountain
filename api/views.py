from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            email_domain = email.split('@')[1]
            if email_domain != "ucsc.edu":
                return JsonResponse({"message": "Require ucsc.edu email", }, status=400)

            password = form.cleaned_data["password"]

            if User.objects.filter(username=email).exists():
                return JsonResponse({"message": "User already exists", }, status=200)

            User.objects.create_user(
                username=email,
                email=email,
                password=password,
            ).save()

            return JsonResponse({"message": "New user created", }, status=200)
        else:
            return JsonResponse({"message": "Invalid form received", }, status=400)

    return JsonResponse({"message": "Request received, but did not satisfy any conditions", }, status=200)


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # User is already logged in
            if request.user.is_authenticated:
                return JsonResponse({"message": "Login success: User already logged in", }, status=200)

            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return JsonResponse({"message": "Login success", }, status=200)
            return JsonResponse({"message": "No user found", }, status=400)
        else:
            return JsonResponse({"message": "Invalid form", }, status=400)

    return JsonResponse({"message": "Invalid login", }, status=400)


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logout successful", }, status=200)
    return JsonResponse({"message": "Require POST request to logout", }, status=400)
