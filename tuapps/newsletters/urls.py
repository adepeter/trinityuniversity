from django.urls import path

from .views import newsletter_subscribe

app_name = 'newsletters'

urlpatterns = [
    path('', newsletter_subscribe, name='newsletter_subscribe'),
]
