"""
Task app URL Configuration

"""

from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>/", views.task_detail_view, name="task-detail"),
    path("", views.task_list_view, name="task-list"),
]
