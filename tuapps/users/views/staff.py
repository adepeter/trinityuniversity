from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView

TEMPLATE_URL = 'users'

User = get_user_model()


class AllStaffListView(ListView):
    model = User
    template_name = f'{TEMPLATE_URL}/staffs_list.html'


class StaffProfileDetailView(DetailView):
    query_pk_and_slug = True
    slug_field = 'username__iexact'
    slug_url_kwarg = 'username'
    model = User
    template_name = f'{TEMPLATE_URL}/staff_profile.html'
