from django import template

from ..models import Degree

register = template.Library()


@register.simple_tag(name='degrees_in_department_by_programme')
def list_degrees_offered_by_department_through_programme(department, programme):
    return Degree.objects.filter(department=department, programme=programme)
