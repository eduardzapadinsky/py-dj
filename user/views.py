from django.shortcuts import render
from django.http import HttpRequest


def user_register(request: HttpRequest):
    return render(request, "user_register.html")


def user_login(request: HttpRequest):
    return render(request, "user_login.html")
