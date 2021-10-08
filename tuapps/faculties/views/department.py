from django.views.generic import DetailView

from ..models import Department

TEMPLATE_URL = 'faculties'


class DepartmentDetailView(DetailView):
    model = Department
    slug_field = 'slug__iexact'
    slug_url_kwarg = 'department'
    template_name = f'{TEMPLATE_URL}/department_detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(faculty__slug__iexact=self.kwargs['faculty'])
