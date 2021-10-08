from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .forms import SubscriberForm


@require_POST
def newsletter_subscribe(request):
    kwargs = {
        'request': request
    }
    current_url = request.POST.get('current_url', '/')
    form = SubscriberForm(data=request.POST, **kwargs)
    if form.is_valid():
        del form.cleaned_data['current_url']
        form.save()
    return redirect(current_url)
