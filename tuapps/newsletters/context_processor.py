from .forms import SubscriberForm


def newsletter_subscriber_form(request):
    kwargs = {
        'request': request
    }
    form = SubscriberForm(**kwargs)
    return {'subscriber_form': form}
