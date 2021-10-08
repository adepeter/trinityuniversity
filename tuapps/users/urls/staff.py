from django.urls import path

from ..views.staff import AllStaffListView, StaffProfileDetailView

app_name = 'staff'

urlpatterns = [
    path('', AllStaffListView.as_view(), name='list_root_staffs'),
    path('<int:id>/<slug:username>/', StaffProfileDetailView.as_view(), name='staff_profile'),
]
