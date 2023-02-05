from django.http import HttpRequest, Http404
from django.shortcuts import render

from blogApp.models import Category

categories = Category.objects.all()


def profile_view(request: HttpRequest):
    return render(request, "profile.html")


def signin_view(request: HttpRequest):
    return render(request, "signin.html")


def signup_view(request: HttpRequest):
    return render(request, "signup.html")
