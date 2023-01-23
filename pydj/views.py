from django.http.request import HttpRequest
from django.http.response import HttpResponse


def homepage_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Домашня сторінка")


def progression_view(request: HttpRequest, start: int, count: int, step: int) -> HttpResponse:
    progression_list = [start]
    x = 1

    while x < count:
        next_value = start + step
        progression_list.append(next_value)
        start = next_value
        x += 1
    progression_list_str = " ".join(str(i) for i in progression_list)

    return HttpResponse(progression_list_str)


def fibonacci_view(request: HttpRequest, n: int):
    next_n = 1
    first_n = 0
    second_n = 1

    for i in range(0, n + 1):
        if i <= 1:
            next_n = i
        else:
            next_n = first_n + second_n
            first_n = second_n
            second_n = next_n
    return HttpResponse(next_n)


def greeting_view(request: HttpRequest, name: str):
    return HttpResponse(f"Greeting, {name.capitalize()}")
