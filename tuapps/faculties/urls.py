from django.urls import path, include

from .views.department import DepartmentDetailView
from .views.faculty import FacultyDetailView

app_name = 'faculties'

urlpatterns = [
    path('<slug:faculty>/', include([
        path('', FacultyDetailView.as_view(), name='faculty_preview'),
        path('<slug:department>/', DepartmentDetailView.as_view(), name='department_preview'),
    ])),
]
