"""
Models for blog

"""
from datetime import datetime

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Blog's category"""

    title: str = models.CharField(max_length=255)
    slug: str = models.SlugField(max_length=255, verbose_name="url", unique=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    """Blog's Post"""
    title: str = models.CharField(max_length=255)
    slug: str = models.SlugField(max_length=255, verbose_name="url", unique=True)
    content: str = models.TextField(blank=True)
    created: datetime = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(auto_now=True)
    category: str = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
