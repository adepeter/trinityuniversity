from django import forms
from django.utils.translation import gettext_lazy as _


class RegistrationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-white',
                'placeholder': _('%(field_label)s' % {'field_label': self.fields[field].label})
            })

    email = forms.EmailField(
        label=_('e-mail')
    )
    username = forms.CharField(
        label=_('username')
    )
    password = forms.CharField(
        label=_('password'),
        widget=forms.PasswordInput
    )
    repeat_password = forms.CharField(
        label=_('repeat password'),
        widget=forms.PasswordInput
    )
    first_name = forms.CharField(
        label=_('first name')
    )
    last_name = forms.CharField(
        label=_('last name')
    )
    accept_terms = forms.BooleanField(
        label=_('accept terms')
    )
