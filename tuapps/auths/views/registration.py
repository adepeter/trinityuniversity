from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

from ..forms.registration import RegistrationForm
from ...users.forms.user import UserRegistrationForm


TEMPLATE_URL = 'auths'

User = get_user_model()

def register(request):
    if request.method == 'POST':
        user_registration_form = UserRegistrationForm(data=request.POST)
        if user_registration_form.is_valid():
            new_user = user_registration_form.save(commit=False)
            new_user.password = user_registration_form.cleaned_data['password']
            new_user.save()
    elif request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        user_registration_form = UserRegistrationForm()
    return render(request, 'registration.html', context={'form': user_registration_form})


class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = f'{TEMPLATE_URL}/registration.html'
