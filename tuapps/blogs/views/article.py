from django.shortcuts import get_list_or_404
from django.views.generic import ListView, DetailView

from ..models import Category, Tag
from ..models.article import Article

TEMPLATE_URL = 'blogs'


class ArticleListView(ListView):
    model = Article
    template_name = f'{TEMPLATE_URL}/articles_list.html'
    paginate_by = 10
    ordering = ['-date_posted']

    def get_queryset(self):
        qs = super().get_queryset()
        try:
            category_name = self.request.GET['category']
            return get_list_or_404(qs, category__name__iexact=category_name)
        except KeyError:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class ArticleDetailView(DetailView):
    query_pk_and_slug = True
    model = Article
    template_name = f'{TEMPLATE_URL}/article_read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.filter(parent__isnull=True)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context
