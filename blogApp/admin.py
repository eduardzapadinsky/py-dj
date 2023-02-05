from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin panel for categories"""

    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title"]
    ordering = ["title"]
    search_fields = ["title"]
    save_as = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin panel for posts"""

    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "content", "created", "updated", "category"]
    list_editable = ["content"]
    ordering = ["-updated"]
    search_fields = ["title", "content"]
    save_on_top = True
    save_as = True
