from django import template
from django.db.models import Q

from ..models import Faculty

register = template.Library()


@register.simple_tag(name='all_faculties_without_children')
def list_all_faculties_without_children():
    """Return lists of all Parent faculties but exclude Parent faculties with children"""
    # either run this or the below
    # Faculty.objects.filter(parent__isnull=True).exclude(children__isnull=False)
    return Faculty.objects.filter(Q(parent__isnull=True) & ~Q(children__isnull=False))


@register.simple_tag(name='all_faculties_that_are_children')
def list_all_faculties_that_are_children():
    """Return lists of all faculties that are children to parent faculties"""
    # either run this or the below
    # Faculty.objects.exclude(parent__isnull=True)
    return Faculty.objects.filter(parent__isnull=False)
