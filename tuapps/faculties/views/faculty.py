from django.views.generic import DetailView

from ..models import Faculty

TEMPLATE_URL = 'faculties'


class FacultyDetailView(DetailView):
    model = Faculty
    slug_field = 'slug__iexact'
    slug_url_kwarg = 'faculty'
    template_name = f'{TEMPLATE_URL}/faculty_detail.html'
