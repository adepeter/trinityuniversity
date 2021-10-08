from django.urls import path

from .views import GalleryView

app_name = 'galleries'

urlpatterns = [
    path('', GalleryView.as_view(), name='galleries')
]
