"""
Task app URL Configuration

"""

from django.urls import path

from . import views

urlpatterns = [
    # path("profile/<str:username>", views.profile_view, name="profile"),
    path("signin/", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
]




