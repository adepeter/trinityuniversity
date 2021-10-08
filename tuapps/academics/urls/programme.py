from django.urls import path

from ..views.programme import ProgrammeListView, ProgrammeDetailView

app_name = 'programme'


urlpatterns = [
    path('', ProgrammeListView.as_view(), name='programmes_list'),
    path('<slug:programme>/', ProgrammeDetailView.as_view(), name='programmes_detail'),
]
