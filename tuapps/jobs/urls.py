from django.urls import path

from .views import JobListView, JobDetailView

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job_listings'),
    path('<int:id>/<slug:slug>/', JobDetailView.as_view(), name='job_preview'),
]
