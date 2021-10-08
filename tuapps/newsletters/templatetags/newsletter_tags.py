from django import template

from ..forms import SubscriberForm

register = template.Library()


@register.inclusion_tag('newsletters/_templatetags/_newsletter_subscriber_form.html')
def newsletter_subscriber_form(request):
    kwargs = {
        'request': request
    }
    form = SubscriberForm(**kwargs)
    return {'form': form}
