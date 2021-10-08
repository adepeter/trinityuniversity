from django import template

from ..models import Programme

register = template.Library()


@register.simple_tag(name='all_programmes')
def list_all_programmes():
    return Programme.objects.all()


@register.simple_tag
def programmes_by_faculty(faculty):
    return faculty.programmes.all()
