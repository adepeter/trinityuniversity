from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'description',
        'parent',
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
