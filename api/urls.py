from django.urls import path

from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('course', views.course, name='course'),
    path('create_review', views.create_review, name='create_review'),
    path('find_review', views.find_review, name='find_review'),
]