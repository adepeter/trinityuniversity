from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    auto_id = False
    current_url = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['current_url'].initial = request.path

    class Meta:
        model = Subscriber
        fields = ['subscriber_email']
        widgets = {
            'subscriber_email': forms.EmailInput(attrs={
                'id': 'email_newsletter',
                'class': 'form-control',
                'placeholder': _('Your Email'),
            })
        }
