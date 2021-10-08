from django import template

from ..models import Department

register = template.Library()


@register.simple_tag(name='other_departments_in_faculty')
def departments_in_faculty(faculty, department):
    return Department.objects.filter(faculty=faculty).exclude(name=department.name)
