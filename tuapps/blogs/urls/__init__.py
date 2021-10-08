from django.urls import path

from ..views.article import ArticleListView, ArticleDetailView

app_name = 'blogs'

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_listing'),
    path('<int:id>/<slug:slug>/', ArticleDetailView.as_view(), name='article_read'),
]
