from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag(filename='blogs/_inclusion/sidebar/categories_list.html')
def list_all_categories():
    return {
        'categories': Category.objects.all()
    }
