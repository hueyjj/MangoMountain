from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm, CourseForm
from .models import Course, SectionLab


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


@csrf_exempt
def course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course_num = form.cleaned_data["course_num"]
            try:
                course = Course.objects.get(class_num=course_num)

                section_and_labs = []
                section_labs_objects = SectionLab.objects.filter(course_num__in=[course.class_num])
                for section_lab in section_labs_objects:
                    section_and_labs.append({
                        "course_num": section_lab.course_num,
                        "class_id": section_lab.class_id,
                        "time": section_lab.time,
                        "instructor": section_lab.instructor,
                        "location": section_lab.location,
                        "enrollment": section_lab.enrollment,
                        "wait": section_lab.wait,
                        "status": section_lab.status,
                    })

                json_course = {
                    "title": course.title,
                    "description": course.description,
                    "class_notes": course.class_notes,
                    "available_seats": course.available_seats,
                    "career": course.career,
                    "class_num": course.class_num,
                    "credits": course.credits,
                    "enrolled": course.enrolled,
                    "enrollment_capacity": course.enrollment_capacity,
                    "general_education": course.general_education,
                    "grading": course.grading,
                    "status": course.status,
                    "type": course.type,
                    "waitlist_capacity": course.waitlist_capacity,
                    "waitlist_total": course.waitlist_total,
                    "days_and_times": course.days_and_times,
                    "instructor": course.instructor,
                    "meeting_dates": course.meeting_dates,
                    "room": course.room,
                    "section_and_labs": section_and_labs,
                }
                return JsonResponse({
                    "message": "Valid course request",
                    "course": json_course
                }, status=200)
            except Course.DoesNotExist:
                return JsonResponse({"message": "Course does not exist", }, status=400)
            return JsonResponse({"message": "Got your course request", }, status=400)
        else:
            return JsonResponse({"message": "Invalid course form - ", "error": form.errors.as_json(), }, status=400)
    return JsonResponse({"message": "Invalid course request", }, status=400)
