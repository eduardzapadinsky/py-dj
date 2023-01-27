from django.shortcuts import render
from django.http import HttpRequest, Http404

tasks = [
    {"id": 1, "title": "Task #1", "description": "Some description1", "created": "2022-01-24 12:00",
     "updated": "2022-01-26 12:00", "completed": False},
    {"id": 2, "title": "Task #2", "description": "Some description2", "created": "2022-01-24 12:00",
     "updated": "2022-01-26 12:00", "completed": True},
    {"id": 3, "title": "Task #3", "description": "Some description3", "created": "2022-01-24 12:00",
     "updated": "2022-01-26 12:00", "completed": False},
    {"id": 4, "title": "Task #4", "description": "Some description4", "created": "2022-01-24 12:00",
     "updated": "2022-01-26 12:00", "completed": True},
    {"id": 5, "title": "Task #5", "description": "Some description5", "created": "2022-01-24 12:00",
     "updated": "2022-01-26 12:00", "completed": False},
]


def task_list_view(request: HttpRequest):
    context = {"tasks": tasks}
    return render(request, "task_list.html", context)


def task_detail_view(request: HttpRequest, id: int):
    for task in tasks:
        if task["id"] == id:
            context = {"task": task}
            return render(request, "task_detail.html", context)
    raise Http404
