from django import template
from blogApp.models import Category

register = template.Library()


@register.inclusion_tag("menu_tpl.html")
def show_menu():
    categories = Category.objects.all()
    return {"categories": categories}
