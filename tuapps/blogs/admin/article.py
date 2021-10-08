from django.contrib import admin

# Register your models here.
from ..models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'slug',
        'is_locked',
        'is_hidden',
        'date_posted',
        'date_modified'
    ]
    prepopulated_fields = {
        'slug': ('title',)
    }
