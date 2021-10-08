from django.views.generic import TemplateView

from .models import Gallery

TEMPLATE_URL = 'galleries'


class GalleryView(TemplateView):
    template_name = f'{TEMPLATE_URL}/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Gallery.objects.all()
        return context
