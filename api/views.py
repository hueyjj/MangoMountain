from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm


@csrf_exempt
def signup(request):
    print("signup: Request received")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valid form received")
        else:
            return HttpResponse("Invalid form received")

    return HttpResponse("Request received")