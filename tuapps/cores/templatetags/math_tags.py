from django import template

register = template.Library()


@register.filter
def remainder(numerator, denominator):
    return denominator // numerator
