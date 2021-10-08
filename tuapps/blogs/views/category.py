from django.views.generic import ListView

from ..models import Category

TEMPLATE_URL = 'blogs'


class CategoryListView(ListView):
    model = Category
    template_name = f'{TEMPLATE_URL}/category_list.html'
