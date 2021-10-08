from django import template

from ..models import Article

register = template.Library()


@register.simple_tag(name='latest_articles')
def get_latest_articles(count=10):
    return Article.objects.all()[:count]
