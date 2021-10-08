from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from tuapps.academics.models import Programme

TEMPLATE_URL = 'academics/degree'


class DegreeListByProgrammeView(SingleObjectMixin, ListView):
    template_name = f'{TEMPLATE_URL}/degree_list_by_programme.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(Programme.objects.all())
        super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.degrees.all()
