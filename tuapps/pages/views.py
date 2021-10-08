from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView

from .forms.visitor import VisitorScheduleForm
from .models import VisitorSchedule

TEMPLATE_URL = 'pages'


class WhyUsView(TemplateView):
    template_name = f'{TEMPLATE_URL}/why_us.html'


class ScheduleVisitView(CreateView):
    model = VisitorSchedule
    form_class = VisitorScheduleForm
    template_name = f'{TEMPLATE_URL}/visit_schedule.html'


class TourView(TemplateView):
    template_name = f'{TEMPLATE_URL}/tour.html'
