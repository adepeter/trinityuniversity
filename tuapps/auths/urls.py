from django.urls import path

from .views.registration import UserRegistrationView

app_name = 'auths'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration')
]
