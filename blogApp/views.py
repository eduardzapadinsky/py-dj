from django.http import HttpRequest, Http404
from django.shortcuts import render

from .models import Post


def post_list_view(request: HttpRequest):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "post_list.html", context)


def post_by_category_view(request: HttpRequest, slug: str):
    try:
        posts = Post.objects.filter(category__slug=slug)
    except Post.DoesNotExist:
        raise Http404("Object not found")
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


def post_by_date_view(request: HttpRequest, slug: str):
    try:
        posts = Post.objects.filter(created__year=slug[:4], created__month=slug[5:])
    except Post.DoesNotExist:
        raise Http404("Object not found")
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


def post_detail_view(request: HttpRequest, slug: str):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Object not found")
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)
