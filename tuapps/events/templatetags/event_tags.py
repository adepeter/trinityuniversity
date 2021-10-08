from django import template

from ..models import Event

register = template.Library()


@register.simple_tag(name='all_events')
def get_all_events(count=10):
    return Event.objects.all()
