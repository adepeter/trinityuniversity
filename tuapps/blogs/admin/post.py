from django.contrib import admin

# Register your models here.
from ..models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'poster',
        'article',
        'is_hidden',
        'date_posted',
        'date_modified'
    ]
