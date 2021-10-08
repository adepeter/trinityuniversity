from django.urls import path, include

from .views import WhyUsView, TourView

app_name = 'pages'

urlpatterns = [
    path('why-us/', WhyUsView.as_view(), name='why_us'),
    path('tour/', TourView.as_view(), name='tour'),
    path('', include('django.contrib.flatpages.urls')),
]
