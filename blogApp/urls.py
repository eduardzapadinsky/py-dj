"""
Task app URL Configuration

"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list_view, name="homepage"),
    path("posts/", views.post_list_view, name="post-list"),
    path("posts/<str:slug>/", views.post_detail_view, name="post-detail"),
    path("category/<str:slug>/", views.post_by_category_view, name="category"),
    path("date/<str:slug>/", views.post_by_date_view, name="date"),
]
